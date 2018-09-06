#!/usr/bin/env python
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
# from elasticsearch.helpers import parallel_bulk


def get_actions():
    index = 'test'
    doc_type = 'dev'
    actions = [
        {
            'id': 1,
            'name': "elasticsearch",
            'description': "elasticsearch is a good database."
        },
        {
            'id': 2,
            'name': "mysql",
            'description': "mysql is a good database."
        },
    ]

    for action in actions:
        yield {
            '_index' : index,
            '_type'  : doc_type,
            '_id'    : action['id'],
            '_source': action
        }


def batch_processing(es):
    data = bulk(es, get_actions())
    # data = parallel_bulk(es, get_actions())
    print(data)


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200'])
    batch_processing(es)


# references
# https://www.elastic.co/guide/en/elasticsearch/reference/current/_batch_processing.html
# http://www.elastic.co/guide/en/elasticsearch/reference/current/docs-bulk.html
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/__init__.py#L1116
# https://stackoverflow.com/questions/20288770/how-to-use-bulk-api-to-store-the-keywords-in-es-by-using-python
# https://github.com/elastic/elasticsearch-py/issues/508
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/helpers/__init__.py#L222