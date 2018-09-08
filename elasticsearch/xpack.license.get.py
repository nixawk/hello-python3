#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from pprint import pprint


def xpack_license_get(es):
    pprint(es.xpack.license.get())
    
    """
    {'license': {'issue_date': '2018-08-22T08:47:25.237Z',
                 'issue_date_in_millis': 1534927645237,
                 'issued_to': 'elasticsearch',
                 'issuer': 'elasticsearch',
                 'max_nodes': 1000,
                 'start_date_in_millis': -1,
                 'status': 'active',
                 'type': 'basic',
                 'uid': '5febbc5c-4d95-448b-b962-a0205326f4ab'}}
    """


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    xpack_license_get(es)



# references
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/xpack/license.py