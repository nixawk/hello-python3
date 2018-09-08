#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from pprint import pprint


def cluster_pending_tasks(es):
    """The pending cluster tasks API returns a list of any cluster-level
    changes (e.g. create index, update mapping, allocate or fail shard)
    which have not yet been executed.
    """
    pprint(es.cluster.pending_tasks())
    


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    cluster_pending_tasks(es)


# references
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/cluster.py#L37
