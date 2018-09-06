#!/usr/bin/python
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch


def deleting_documents(es):
    index = 'test'
    doc_type = 'dev'
    body = {
        'id': 1,
        'name': "elasticsearch",
        'description': "elasticsearch is a good database. It's updated."
    }
    if es.exists(index, doc_type, body['id']):
        data = es.delete(index, doc_type, body['id'])
        print(data)


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200'])
    deleting_documents(es)


# references
# https://www.elastic.co/guide/en/elasticsearch/reference/current/_deleting_documents.html
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/__init__.py#L1041
