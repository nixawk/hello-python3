#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch


def get_all_indexes(es):
    for index in es.indices.get_alias('*').keys():
        print(index)


def delete_an_index(es, index):
    print(es.indices.delete(index))  # {'acknowledged': True}


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200'])
    get_all_indexes(es)

    # delete_an_index(es, ".monitoring-es-6-2018.08.24")


# references
# https://www.elastic.co/guide/en/elasticsearch/reference/current/_delete_an_index.html
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/indices.py#L166