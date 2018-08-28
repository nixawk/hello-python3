#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch

def list_all_indices(es):
    print(es.indices.stats())
    es.indices.get_alias('*')


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200'])
    list_all_indices(es)

# references
# https://www.elastic.co/guide/en/elasticsearch/reference/current/_list_all_indices.html
# https://github.com/elastic/elasticsearch-py
