#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from pprint import pprint


def remote_info(es):
    pprint(es.remote.info())

    
if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    remote_info(es)


# references
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/remote.py