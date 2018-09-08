#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HEAD /test/_mapping/dev HTTP/1.1
Host: 127.0.0.1:9200
Accept-Encoding: identity
connection: keep-alive
content-type: application/json

HTTP/1.1 404 Not Found
content-type: application/json; charset=UTF-8
content-length: 237
"""

from elasticsearch import Elasticsearch


def indices_exists_type(es):
    index = 'test'
    doc_type = 'dev'

    print(es.indices.exists_type(index, doc_type))


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    indices_exists_type(es)


# references
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/indices.py#L214