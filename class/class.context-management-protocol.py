#!/usr/bin/python
# -*- coding: utf-8 -*-

from functools import partial
import socket


class LazyConnection(object):

    def __init__(self, address, family=socket.AF_INET, socktype=socket.SOCK_STREAM):
        self.address = address
        self.family = family
        self.socktype = socktype
        self.sock = None

    def __enter__(self):
        if self.sock is not None: raise RuntimeError('Already connected')

        self.sock = socket.socket(self.family, self.socktype)
        self.sock.connect(self.address)

        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


if __name__ == '__main__':
    with LazyConnection(('www.python.org', 80)) as conn:
        conn.send(b'GET /index.html HTTP/1.0\r\n')
        conn.send(b'Host: www.python.org\r\n')
        conn.send(b'\r\n')

        resp = b''.join(iter(partial(conn.recv, 8192), b''))
        print(resp)