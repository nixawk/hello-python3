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
        self.connections = []

    def __enter__(self):
        self.sock = socket.socket(self.family, self.socktype)
        self.sock.connect(self.address)
        self.connections.append(self.sock)

        return self.sock

    def __exit__(self, *exc):
        self.sock = self.connections.pop()
        self.sock.close()
        self.sock = None


if __name__ == '__main__':
    with LazyConnection(('www.python.org', 80)) as conn1:
        conn1.send(b'GET /index.html HTTP/1.0\r\n')
        conn1.send(b'Host: www.python.org\r\n')
        conn1.send(b'\r\n')

        func = partial(conn1.recv, 8192)
        data = b"".join(iter(func, b''))
        print(data)