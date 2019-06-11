#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
import threading
import json


class FakeResponse(object):
    def __init__(self, filename='chrome-browser.har'):
        self.entries = None
        with open(filename) as f:
            jsondata = jsondata = json.load(f)
            log = jsondata.get('log')
            # log.keys()
            # dict_keys(['version', 'creator', 'pages', 'entries'])

            self.entries = log.get('entries')

    def filter_entries(self, url):
        entries = list(
            filter(
                lambda x: x.get('request').get('url') == url,
                self.entries
            )
        )

        return list(
            filter(
                lambda x: len(x.get('response').get('content').get('text', '')) > 0,
                entries
            )
        )


FAKERESPONSE = FakeResponse()

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Support HTTP Method.
        """
        # (Pdb) self.requestline
        # 'GET http://www.apache.org/ HTTP/1.1'

        # (Pdb) self.command
        # 'GET'

        # (Pdb) self.path
        # 'http://www.apache.org/'

        # (Pdb) self.request_version
        # 'HTTP/1.1'

        # (Pdb) self.headers
        # <http.client.HTTPMessage object at 0x7f320fa9cc50>

        # -----------------------------------------------------------

        # (Pdb) self.path
        # 'http://www.apache.org/xxx/yyy/zzz/?query=msg'
        # (Pdb) self.requestline
        # 'GET http://www.apache.org/xxx/yyy/zzz/?query=msg HTTP/1.1'

        self.send_response(200)
        self.end_headers()

        entries = FAKERESPONSE.filter_entries(self.path)
        message = b''

        if len(entries) > 0:
            content_text = entries[0].get('response').get('content', {}).get('text', '')
            message = content_text.encode()

        self.wfile.write(message)
        self.wfile.write(b'\n')
        return
    
    def do_POST(self):
        """Support POST Method.
        """
        self.do_GET()

    def do_HEAD(self):
        """Support HEAD Method.
        """
        self.do_GET()


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
    pass


if __name__ == '__main__':
    server = ThreadedHTTPServer(('0.0.0.0', 8080), Handler)
    print('Starting server, use <Ctrl-C> to stop')
    server.serve_forever()


# references
# https://stackoverflow.com/questions/14088294/multithreaded-web-server-in-python