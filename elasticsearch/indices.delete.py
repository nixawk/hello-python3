#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
DELETE /test HTTP/1.1
Host: 127.0.0.1:9200
Accept-Encoding: identity
connection: keep-alive
content-type: application/json

HTTP/1.1 200 OK
content-type: application/json; charset=UTF-8
content-length: 21

{"acknowledged":true}
"""

from elasticsearch import Elasticsearch


def indices_delete(es):
    """Create an index in Elasticsearch.
    """
    index = "test"
    if (es.indices.exists(index)):
        print("index: %s exists" % index)
        data = es.indices.delete(index)
        print(data)
    

if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    indices_delete(es)


# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/indices.py#L166
