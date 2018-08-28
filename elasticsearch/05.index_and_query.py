#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch


def index_and_query(es):
    index = 'test'
    doc_type = 'dev'
    body = {
        'id': 1,
        'name': "elasticsearch",
        'description': "elasticsearch is a good database."
    }

    es.index(index, doc_type, body, id=body.get('id'))
    print(es.search(index=index))
    print(es.search(index=index, doc_type=doc_type))

    """
    {'_shards': {'failed': 0, 'skipped': 0, 'successful': 5, 'total': 5},
     'hits': {'hits': [{'_id': 'opsKgWUBzglVwuK2cjWn',
                        '_index': 'test',
                        '_score': 1.0,
                        '_source': {'description': 'elasticsearch is a good '
                                                   'database',
                                    'name': 'elasticsearch'},
                        '_type': 'dev'},
                       {'_id': 'oZsKgWUBzglVwuK2YjWn',
                        '_index': 'test',
                        '_score': 1.0,
                        '_source': {'description': 'elasticsearch is a good '
                                                   'database',
                                    'name': 'elasticsearch'},
                        '_type': 'dev'},
                       {'_id': '1',
                        '_index': 'test',
                        '_score': 1.0,
                        '_source': {'description': 'elasticsearch is a good '
                                                   'database.',
                                    'id': 1,
                                    'name': 'elasticsearch'},
                        '_type': 'dev'},
                       {'_id': 'o5sLgWUBzglVwuK2CTXx',
                        '_index': 'test',
                        '_score': 1.0,
                        '_source': {'description': 'elasticsearch is a good '
                                                   'database',
                                    'name': 'elasticsearch'},
                        '_type': 'dev'},
                       {'_id': 'pJsLgWUBzglVwuK2EzWW',
                        '_index': 'test',
                        '_score': 1.0,
                        '_source': {'description': 'elasticsearch is a good '
                                                   'database',
                                    'name': 'elasticsearch'},
                        '_type': 'dev'}],
              'max_score': 1.0,
              'total': 5},
     'timed_out': False,
     'took': 3}
    """


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200'])
    index_and_query(es)

# references
# https://www.elastic.co/guide/en/elasticsearch/reference/current/_index_and_query_a_document.html
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/__init__.py
