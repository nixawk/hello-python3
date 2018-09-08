#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from pprint import pprint


def snapshot_status(es):
    pprint(es.snapshot.status())


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    snapshot_status(es)


# references
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/snapshot.py