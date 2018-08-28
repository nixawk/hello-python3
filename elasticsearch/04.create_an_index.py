#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch


def create_an_index(es):
    index = 'test'
    doc_type = 'dev'
    doc_id = 1
    body = {
        'name': "elasticsearch",
        'description': "elasticsearch is a good database",
    }

    # es.delete(index, doc_type, doc_id)
    # es.create(index, doc_type, doc_id, body)
    
    es.index(index, doc_type, body)
    print(es.cat.indices())


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200'])
    create_an_index(es)

# references
# https://www.elastic.co/guide/en/elasticsearch/reference/current/_create_an_index.html
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/__init__.py