#!/usr/bin/python
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch


def get_cluster_health(es):
    """To check the cluster health, we will be using the _cat API.

    GET /_cat/health?v
    """
    # es.cluster.allocation_explain
    # es.cluster.client
    # es.cluster.get_settings
    # es.cluster.health
    # es.cluster.pending_tasks
    # es.cluster.put_settings
    # es.cluster.reroute
    # es.cluster.state
    # es.cluster.stats
    # es.cluster.transport
    print(es.cluster.health())


def get_nodes_info(es):
    # es.nodes.client
    # es.nodes.hot_threads
    # es.nodes.info
    # es.nodes.stats
    # es.nodes.transport
    # es.nodes.usage
    print(es.nodes.info())


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200'])

    print("\n----Cluster Health\n")
    get_cluster_health(es)

    print("\n----Nodes Info\n")
    get_nodes_info(es)


# references
# https://www.elastic.co/guide/en/elasticsearch/reference/current/_cluster_health.html
