#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch


def cat_repositories(es):
    print(es.cat.repositories())
    

if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    cat_repositories(es)


# references
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/cat.py#L361