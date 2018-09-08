#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch


def cat_count(es):
    """Count provides quick access to the document count of the entire cluster,
    or individual indices.
    """
    print(es.cat.allocation())
    

if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    cat_count(es)


# references
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/cat.py#L52