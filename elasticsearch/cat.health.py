#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch


def cat_health(es):
    """health is a terse, one-line representation of the same information.
    """
    print(es.cat.health())
    

if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    cat_health(es)


# references
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/cat.py#L76