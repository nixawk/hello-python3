#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from pprint import pprint


def cluster_state(es):
    """Get a comprehensive state information of the whole cluster.
    """
    pprint(es.cluster.state())


def cluster_stats(es):
    """he Cluster Stats API allows to retrieve statistics from a cluster wide
    perspective. The API returns basic index metrics and information about
    the current nodes that form the cluster.
    """
    pprint(es.cluster.stats())


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    cluster_state(es)
    cluster_stats(es)


# references
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/cluster.py#L53