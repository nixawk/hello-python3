#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch


def indices_create(es):
    """Create an index in Elasticsearch.
    """
    index = "test"
    if (es.indices.exists(index)):
        print("index: %s exists" % index)
    else:
        data = es.indices.create(index)
        print(data)
    

if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    indices_create(es)


# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/indices.py#L73