#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

from elasticsearch import Elasticsearch


def indices_exists(es):
    """Return a boolean indicating whether given index exists.
    """
    index = "test"
    if (es.indices.exists(index)):
        print("index: %s exists" % index)
    else:
        print("index: %s not exists" % index)
    

if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    indices_exists(es)


# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/indices.py#L189