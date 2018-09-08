#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch
from pprint import pprint


def cluster_health(es):
    """Get a very simple status on the health of the cluster.
    """
    pprint(es.cluster.health())
    
    """
    {'active_primary_shards': 15,
     'active_shards': 15,
     'active_shards_percent_as_number': 60.0,
     'cluster_name': 'elasticsearch',
     'delayed_unassigned_shards': 0,
     'initializing_shards': 0,
     'number_of_data_nodes': 1,
     'number_of_in_flight_fetch': 0,
     'number_of_nodes': 1,
     'number_of_pending_tasks': 0,
     'relocating_shards': 0,
     'status': 'yellow',
     'task_max_waiting_in_queue_millis': 0,
     'timed_out': False,
     'unassigned_shards': 10}
    """
    

if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    cluster_health(es)


# references
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/cluster.py#L8