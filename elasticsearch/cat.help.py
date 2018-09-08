#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
=^.^=
/_cat/allocation
/_cat/shards
/_cat/shards/{index}
/_cat/master
/_cat/nodes/_cat/tasks
/_cat/indices
/_cat/indices/{index}
/_cat/segments
/_cat/segments/{index}
/_cat/count/_cat/count/{index}/_cat/recovery
/_cat/recovery/{index}
/_cat/health
/_cat/pending_tasks
/_cat/aliases
/_cat/aliases/{alias}
/_cat/thread_pool
/_cat/thread_pool/{thread_pools}
/_cat/plugins
/_cat/fielddata
/_cat/fielddata/{fields}
/_cat/nodeattrs
/_cat/repositories
/_cat/snapshots/{repository}
/_cat/templates
"""

from elasticsearch import Elasticsearch


def cat_help(es):
    """A simple help for the cat api..
    """
    print(es.cat.help())
    

if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    cat_help(es)


# references
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/cat.py#L98