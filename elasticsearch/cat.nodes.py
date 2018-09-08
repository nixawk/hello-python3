#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch


def cat_nodes(es):
    """The nodes command shows the cluster topology.
    """
    print(es.cat.nodes())


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    cat_nodes(es)


# references
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/cat.py#L321