#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 1. sudo pip install awscli
# 2. aws configure
# 3. aws route53 list-hosted-zones
# 4. aws route53 list-resource-record-sets --hosted-zone-id XXXXXXXXXXXX
# 5. alarm

# {  "Type" : "A" }
# {  "Type" : "AAAA" }
# {  "Type" : "CNAME" }
# {  "Type" : "MX" }
# {  "Type" : "NS" }
# {  "Type" : "PTR" }
# {  "Type" : "SOA" }
# {  "Type" : "SPF" }
# {  "Type" : "SRV" }
# {  "Type" : "TXT" }


import logging
import boto3
import pymongo


logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__file__)


class AmazonRoute53Exception(Exception):
    """ AmazonRoute53Exception
    """
    pass


class AmazonRoute53(object):
    """Amazon Route 53 is a highly available and scalable Name System (DNS)
    web service.
    """

    def __init__(self, *args, **kwargs):
        super()

        assert 'aws_access_key_id' in kwargs.keys(), AmazonRoute53Exception(
            "please set aws_access_key_id")
        assert 'aws_secret_access_key' in kwargs.keys(), AmazonRoute53Exception(
            "please set aws_secret_access_key")

        self.mgo_client = pymongo.MongoClient(
            host=kwargs.get('mongodb_host', 'localhost'),
            port=kwargs.get('mongodb_port', 27017)
        )

        self.mgo_database = self.mgo_client.get_database(
            kwargs.get('mongodb_database', 'domains')
        )

        self.mgo_collection = self.mgo_database.get_collection(
            kwargs.get('mongodb_collection', 'aws')
        )

        self.aws_client = boto3.client(
            'route53',
            aws_access_key_id=kwargs.get('aws_access_key_id'),
            aws_secret_access_key=kwargs.get('aws_secret_access_key')
        )

        self.hosted_zones = None
        self.hosted_zones_ids = []

    def dump(self):
        """dump all record sets in all hosted zones.
        """
        LOG.info("[*] starts to dump all domains details")
        self.dump_hosted_zones()
        for hosted_zone_id in self.hosted_zones_ids:
            for resource_record_set in self.dump_record_sets(hosted_zone_id):
                resource_record_set['HostedZoneId'] = hosted_zone_id  # Fix NS bug
                self.save_record_set(resource_record_set)

    def dump_hosted_zones(self, max_items=100):
        """dump hosted zones.

        https://console.aws.amazon.com/route53/home#hosted-zones:
        """
        LOG.info("[*] dump hosted-zones")

        self.hosted_zones = self.aws_client.list_hosted_zones(
            MaxItems=str(max_items),
        )

        if not self.hosted_zones:
            return

        for hosted_zone in self.hosted_zones.get('HostedZones'):
            hz_Id = hosted_zone.get('Id')  # /hostedzone/Z3K4F9NBCYAAAH
            # hz_Name = hosted_zone.get('Name')  # example.com

            # The Route 53 Hosted Zone ID column shows the Route 53 Hosted Zone IDs
            # for the API Gateway regional endpoints.
            if not hz_Id.startswith("/hostedzone/"):
                continue

            _, hosted_zone_id = hz_Id.split("/hostedzone/", maxsplit=2)
            if hosted_zone_id not in self.hosted_zones_ids:
                self.hosted_zones_ids.append(hosted_zone_id)

    def dump_record_sets(self, hosted_zone_id, max_items=200):
        """dump record sets.

        https://console.aws.amazon.com/route53/home#resource-record-sets:XXXXXXXXXXXX
        """
        LOG.info("[*] dump resource-record-sets, hosted-zone-id: %s" % hosted_zone_id)

        response = self.aws_client.list_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            MaxItems=str(max_items)
        )

        for resource_record_set in response.get('ResourceRecordSets'):
            yield resource_record_set

    def save_record_set(self, resource_record_set):
        """save resource_record_set into mongodb database.
        """
        LOG.info("[+] save_record_set: %s" % str(resource_record_set))

        recode_type = resource_record_set.get('Type')

        filter_opt = {
            'HostedZoneId': resource_record_set.get('HostedZoneId'),  # uniq Hosted-Zone
            'Name': resource_record_set.get('Name'),
            'Type': recode_type,
        }

        # CNAME(s)
        if recode_type.upper() == 'CNAME' and 'SetIdentifier' in resource_record_set:
            filter_opt['SetIdentifier'] = resource_record_set.get('SetIdentifier')

        return_val = self.mgo_collection.find_one(filter_opt)

        # If exists, return a document.
        # If not exists, return None

        # If no document, insert a new document
        if not return_val:
            LOG.info("insert a new document")
            self.mgo_collection.insert_one(resource_record_set)
            return

        # If a document, check if the document needs to be updated.
        return_val.pop('_id')

        # return_val           : previous document from mongodb
        # resource_record_set  : current document from aws
        self.check_and_alarm(return_val, resource_record_set)

        # always update the document
        update_val = {
            "$set": resource_record_set
        }

        self.mgo_collection.update(filter_opt, update_val)

    def check_and_alarm(self, previous_doc, current_doc):
        """compare all key(s), and alarm the different key.
        """
        LOG.info("[+] compare_and_alarm")

        alarm_info = {
            'HostedZoneId': current_doc.get('HostedZoneId'),  # uniq Hosted-Zone
            'Name': previous_doc.get('Name'),
            'Type': previous_doc.get('Type'),
            'Acts': []
        }

        sp_keys = set(previous_doc.keys())
        sc_keys = set(current_doc.keys())

        del_mid_key = '_id'

        if del_mid_key in sp_keys:
            sp.keys.remove(del_mid_key)

        if del_mid_key in sc_keys:
            sc_keys.remove(del_mid_key)

        p_sub_c = sp_keys - sc_keys
        c_sub_p = sc_keys - sp_keys

        update_keys = []  # record update keys
        delete_keys = []  # record delete keys
        insert_keys = []  # record insert keys

        # Check update action(s)
        if len(p_sub_c) == 0:
            for k in sp_keys:
                pk_val = previous_doc[k]
                ck_val = current_doc[k]

                # SOA / NS
                if isinstance(pk_val, list):
                    _pk_val = sorted([_.get('Value') for _ in pk_val])
                    _ck_val = sorted([_.get('Value') for _ in ck_val])

                    pk_val = _pk_val
                    ck_val = _ck_val

                # record not updated
                if pk_val == ck_val:
                    continue

                # record updated
                _kv = {k: {'previous': pk_val, 'current': ck_val}}
                if _kv not in update_keys:
                    update_keys.append(_kv)

        # Check delete action(s)
        elif len(p_sub_c) > 0:
            for k in p_sub_c:
                _kv = {k: previous_doc.get(k)}
                if _kv not in delete_keys:
                    delete_keys.append(_kv)

            # delete_keys = [str(_) for _ in p_sub_c]

        # Check insert action(s)
        elif len(c_sub_p) > 0:
            for k in c_sub_p:
                _kv = {k: current_doc.get(k)}
                if _kv not in insert_keys:
                    insert_keys.append(_kv)

            # insert_keys = [str(_) for _ in c_sub_p]

        if len(update_keys) > 0:  # has update action(s)
            alarm_info['Acts'].append({'update': update_keys})

        if len(delete_keys) > 0:  # has delete action(s)
            alarm_info['Acts'].append({'delete': update_keys})

        if len(insert_keys) > 0:  # has insert action(s)
            alarm_info['Acts'].append({'insert': update_keys})

        if len(alarm_info['Acts']) > 0:
            LOG.warn("[!] find an alarm: %s" % str(alarm_info))
            self.mgo_database.get_collection('alarms').insert_one(alarm_info)

        return alarm_info


def main():
    config = {
        'mongodb_host': 'localhost',
        'mongodb_port': 27017,
        'mongodb_database': 'domains',
        'mongodb_collection': 'aws',
        'aws_access_key_id': 'your aws access key id',
        'aws_secret_access_key': 'your aws secret access key'
    }
    awsr53 = AmazonRoute53(**config)
    awsr53.dump()


if __name__ == '__main__':
    main()


# references
# https://docs.aws.amazon.com/Route53/latest/APIReference/Welcome.htmls
# https://docs.aws.amazon.com/Route53/latest/APIReference/API-actions-by-function.html
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/route53.html
# https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html#cli-quick-configuration
# https://docs.aws.amazon.com/general/latest/gr/rande.html
# https://docs.mongodb.com/manual/reference/method/db.collection.findOneAndUpdate/
