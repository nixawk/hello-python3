#!/usr/bin/python
# -*- coding: utf-8 -*-

# author: nixawk

from __future__ import print_function
from __future__ import unicode_literals

import xmltodict
import base64


def yield_burpsuite_item(items):
    """return burpsuite item(s) based on python generator"""
    item = items.get('item')

    if isinstance(item, list):    # multi items
        for _ in item:
            yield _

    elif isinstance(item, dict):  # only one item
        yield item


def parse_burpsuite_xml(filename):
    """parse burpsuite history xml file"""
    with open(filename) as xmlfile:
        xmldata = xmlfile.read()
        xmljson = xmltodict.parse(xmldata)

        # burpVersion = items.get('burpVersion')
        # exportTime = items.get('exportTime')
        items = xmljson.get('items')

        for item in yield_burpsuite_item(items):

            # method = item.get('method')
            # host = item.get('host').get('#text')
            # port = item.get('port')
            # url = item.get('url')
            request = item.get('request').get('#text')
            response = item.get('response').get('#text')

            print(base64.b64decode(request))
            if response:
                print(base64.b64decode(response))
            print('----')

    # {u'comment': None,
    #  u'extension': u'txt',
    #  u'host': OrderedDict([(u'@ip', u''), ('#text', u'detectportal.firefox.com')]),
    #  u'method': u'GET',
    #  u'mimetype': None,
    #  u'path': u'/success.txt',
    #  u'port': u'80',
    #  u'protocol': u'http',
    #  u'request': OrderedDict([(u'@base64', u'true'), ('#text', u'R0VUIC9zdWNjZXNzLnR4dCBIVFRQLzEuMQ0KSG9zdDogZGV0ZWN0cG9ydGFsLmZpcmVmb3guY29tDQpVc2VyLUFnZW50OiBNb3ppbGxhLzUuMCAoWDExOyBVYnVudHU7IExpbnV4IHg4Nl82NDsgcnY6NjAuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC82MC4wDQpBY2NlcHQ6ICovKg0KQWNjZXB0LUxhbmd1YWdlOiBlbi1HQixlbjtxPTAuNQ0KQWNjZXB0LUVuY29kaW5nOiBnemlwLCBkZWZsYXRlDQpDYWNoZS1Db250cm9sOiBuby1jYWNoZQ0KUHJhZ21hOiBuby1jYWNoZQ0KQ29ubmVjdGlvbjogY2xvc2UNCg0K')]),
    #  u'response': OrderedDict([(u'@base64', u'true')]),
    #  u'responselength': None,
    #  u'status': None,
    #  u'time': u'Thu Jun 28 09:06:45 CST 2018',
    #  u'url': u'http://detectportal.firefox.com/success.txt'}


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("[*] Usage: %s <1.xml> <2.xml> ..." % sys.argv[0])
        sys.exit(0)

    for _ in sys.argv[1:]:
        parse_burpsuite_xml(_)

## Reference
# https://portswigger.net/burp/help/suite_functions_savingstate
# https://support.portswigger.net/customer/portal/questions/11557016-how-do-i-read-the-burp-saved-state-

