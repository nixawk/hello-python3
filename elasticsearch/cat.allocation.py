#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch


def cat_allocation(es):
    """Allocation provides a snapshot of how shards have located around the
    cluster and the state of disk usage.
    """
    print(es.cat.allocation())
    

if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    cat_allocation(es)


# references
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/cat.py#L27