#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PUT /test/_mapping/dev HTTP/1.1
Host: 127.0.0.1:9200
Accept-Encoding: identity
Content-Length: 133
connection: keep-alive
content-type: application/json

{"customer":{"mappings":{"_doc":{"properties":{"name":{"type":"text","fields":{"keyword":{"type":"keyword","ignore_above":256}}}}}}}}HTTP/1.1 400 Bad Request
content-type: application/json; charset=UTF-8
content-length: 465

{"error":{"root_cause":[{"type":"mapper_parsing_exception","reason":"Root mapping definition has unsupported parameters:  [customer : {mappings={_doc={properties={name={type=text, fields={keyword={type=keyword, ignore_above=256}}}}}}}]"}],"type":"mapper_parsing_exception","reason":"Root mapping definition has unsupported parameters:  [customer : {mappings={_doc={properties={name={type=text, fields={keyword={type=keyword, ignore_above=256}}}}}}}]"},"status":400}
"""

from elasticsearch import Elasticsearch


def indices_put_mapping(es):
    """Register specific mapping definition for a specific type.
    """
    index = 'test'
    doc_type = 'dev'
    body = {
        'customer': {
            'mappings': {
                '_doc': {
                    'properties': {
                        'name': {
                            'type': 'text', 
                            'fields': {
                                'keyword': {
                                    'type': 'keyword', 
                                    'ignore_above': 256
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    print(es.indices.put_mapping(doc_type, body, index=index))


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200/'])
    indices_put_mapping(es)


# references
# https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-put-mapping.html
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/indices.py#L241
# https://stackoverflow.com/questions/31635828/python-elasticsearch-client-set-mappings-during-create-index