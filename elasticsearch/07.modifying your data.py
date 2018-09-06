#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from elasticsearch import Elasticsearch


def modifying_your_data(es):
    index = 'test'
    doc_type = 'dev'
    body = {
        'id': 1,
        'name': "elasticsearch",
        'description': "elasticsearch is a good database. It's updated."
    }

    data = es.update(index, doc_type, body['id'], body={'doc': body})
    print(data)


if __name__ == '__main__':
    es = Elasticsearch(['http://127.0.0.1:9200'])
    modifying_your_data(es)


# error

"""
  File "07.modifying your data.py", line 21, in <module>    modifying_your_data(es)  File "07.modifying your data.py", line 16, in modifying_your_data    es.indices.put_mapping(doc_type, body, index=index)  File "/usr/local/lib/python3.6/dist-packages/elasticsearch/client/utils.py", line 76, in _wrapped
    return func(*args, params=params, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/elasticsearch/client/indices.py", line 266, in put_mapping
    '_mapping', doc_type), params=params, body=body)
  File "/usr/local/lib/python3.6/dist-packages/elasticsearch/transport.py", line 318, in perform_request
    status, headers_response, data = connection.perform_request(method, url, params, body, headers=headers, ignore=ignore,
timeout=timeout)
  File "/usr/local/lib/python3.6/dist-packages/elasticsearch/connection/http_urllib3.py", line 186, in perform_request
    self._raise_error(response.status, raw_data)
  File "/usr/local/lib/python3.6/dist-packages/elasticsearch/connection/base.py", line 125, in _raise_error
    raise HTTP_EXCEPTIONS.get(status_code, TransportError)(status_code, error_message, additional_info)
elasticsearch.exceptions.RequestError: RequestError(400, 'mapper_parsing_exception', "Root mapping definition has unsupport
ed parameters:  [id : 1] [name : elasticsearch] [description : elasticsearch is a good database. It's updated by put_mappin
g.]")
"""

"""
POST http://127.0.0.1:9200/test/dev/1/_update [status:400 request:0.007s]
Traceback (most recent call last):
  File "07.modifying your data.py", line 22, in <module>    modifying_your_data(es)  File "07.modifying your data.py", line 16, in modifying_your_data    data = es.update(index, doc_type, body['id'], body=body)  File "/usr/local/lib/python3.6/dist-packages/elasticsearch/client/utils.py", line 76, in _wrapped
    return func(*args, params=params, **kwargs)
  File "/usr/local/lib/python3.6/dist-packages/elasticsearch/client/__init__.py", line 547, in update
    doc_type, id, '_update'), params=params, body=body)
  File "/usr/local/lib/python3.6/dist-packages/elasticsearch/transport.py", line 318, in perform_request
    status, headers_response, data = connection.perform_request(method, url, params, body, headers=headers, ignore=ignore,
timeout=timeout)
  File "/usr/local/lib/python3.6/dist-packages/elasticsearch/connection/http_urllib3.py", line 186, in perform_request
    self._raise_error(response.status, raw_data)
  File "/usr/local/lib/python3.6/dist-packages/elasticsearch/connection/base.py", line 125, in _raise_error
    raise HTTP_EXCEPTIONS.get(status_code, TransportError)(status_code, error_message, additional_info)
elasticsearch.exceptions.RequestError: RequestError(400, 'action_request_validation_exception', 'Validation Failed: 1: scri
pt or doc is missing;')
"""
    
# references
# https://www.elastic.co/guide/en/elasticsearch/reference/current/_modifying_your_data.html
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/indices.py#L241
# https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-put-mapping.html
# https://stackoverflow.com/questions/30598152/how-to-update-a-document-using-elasticsearch-py
# https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/client/__init__.py#L504