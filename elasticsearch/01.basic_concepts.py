#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sudo pip install elasticsearch
from __future__ import print_function
from __future__ import unicode_literals
from pprint import pprint

from elasticsearch import Elasticsearch

# NRT
# Cluster
# Node
# Index
# Type
# Document
# Shards & Replicas

def print_elasticsearch_info():
    print(
        "[*] What's the cluster ?\n\n"
        "A cluster is a collection of one or more nodes (services) that toget"
        "her holds your entire data and provides federated indexing and search "
        "capabilities across all nodes. A cluster is identifier by a unique "
        "name which by default is 'elasticsearch'. This name is important "
        "because a node can only be part of a cluster if the node is set up "
        "to join the cluster by its name. \n"
        "Make sure that you don't reuse the same cluster names in different "
        "environments, otherwise you might end up with nodes joining the wrong "
        "cluster. For instance you could use logging-dev, logging-stage, and "
        "logging-prod for the development, staging, and production clusters.\n\n"
        "Note that it is valid and perfectly fine to have a cluster with only "
        "a single node in it. Furthermore, you may also have multiple "
        "independent clusters each with its own unique cluster name\n"
    )


    print(
        "[*] What's the node ?\n\n"
        "A node is a single server that is part of your cluster, stores your "
        "data, and participates in the cluster's indexing and search "
        "capabilities. Just like a cluster, a node is identified by a name "
        "which by default is a random Universally Unique IDentifier (UUID) that "
        "is assigned to the node at startup. You can define any node name you "
        "want if you do not want the default. This name is important for "
        "administration purposes where you want to identify which servers "
        "in your network correspond to which nodes in your Elasricsearch "
        "cluster.\n"
        "A node can be configured to join a specific cluster by the cluster "
        "name. By default, each node is set up to join a cluster named "
        "elasticsearch which means that if you start up a number of nodes on "
        "your network and --assuming they can discover each other--they "
        "will automatically form and join a single cluster named elasticsearch.\n"
        "In a single cluster, you can have as many nodes as you want. "
        "Furthermore, if there are no other Elasticsearch nodes currently "
        "running on your network, starting a single node "
        "will by default form a new single-node cluster named elasticsearch.\n"
    )

    print(
        "[*] What's the index?\n\n"
        "An Index is a collection of documents that have somewhat similar "
        "characteristics. For example, you can have an index for custormer "
        "data, another index for a product catalog, and yet another inder "
        "for order data. An index is identified by a name (that must be all"
        "lowercase) and this name is used to refer to the index when performing"
        "indexing, search, update, and delete operations against the documents"
        " it.\n"
    )

    print(
        "[*] What's the type?"
        "A type used to be a logical category/partition of your index to allow "
        "you to store different types of documents in the same index, eg one "
        "type for users, another type for blog posts. It is no longer possible "
        "to create multiple types in an index, and the whole concept of types "
        "will be removed in a later version.\n\n"
    )

    print(
        "[*] What's the document?\n\n"
        "A document is a basic unit of information that can be indexed. For "
        "example, you can have a document for a single custormer, another "
        "document for a single product, and yet another for a single order."
        "This document is expressed in JSON (Javascript Object Notation) "
        "which is a ubiquitous internal data interchange format.\n"
        "Within an index/type, you can store as many documents as you want."
        "Note that although a document physically resides in an index, a"
        "document actually must be indexed/assigned to a type inside an index.\n"
    )

    print(
        "[*] What's the Shards & Replicas ?\n\n"
        "An index can potentially store a large amount of data that can exceed"
        "the hardware limits of a single node. For example, a single index of "
        "a billion documents taking up 1TB of disk space may not fit on the "
        "the disk of a single node or may be too slow to serve search requests "
        "from a single node alone.\n"
        "To solve this problem, Elasticsearch provides the ability to subdivide "
        "your index into multiple pieces called shards. When you create an index,"
        "you can simply define the number of shards that you want. Each shard "
        "is in itself a fully-functional and independent 'index' that can be "
        "hosted on any node in the cluster.\n"
        "Sharding is important for two primary reasons:\n"
        "* It allows you to horizontally split/scale your content volume\n"
        "* It allows you to distribute and parallelize operations across shards "
        "(potentially on multiple nodes) thus incresing performance/throughput.\n"
    )

    es = Elasticsearch(['http://localhost:9200/'])
    print('[*] Elasticsearch Information\n')
    pprint(es.info())


if __name__ == '__main__':
    print_elasticsearch_info()

# References
# https://elasticsearch-py.readthedocs.io/en/master/
# https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
