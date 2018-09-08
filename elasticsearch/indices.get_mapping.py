#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
$ python3 indices.get_mapping.py
{'customer': {'mappings': {'_doc': {'properties': {'name': {'type': 'text', 'fields': {'keyword': {'type': 'keyword', 'igno
re_above': 256}}}}}}}}
"""

from elasticsearch import Elasticsearch


def indices_get_mapping(es):
    """Register specific mapping definition for a specific type.
    """
    index = 'customer'

    print(es.indices.get_mapping(index=index))


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    indices_get_mapping(es)


# references
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/indices.py#L241
# https://stackoverflow.com/questions/31635828/python-elasticsearch-client-set-mappings-during-create-index