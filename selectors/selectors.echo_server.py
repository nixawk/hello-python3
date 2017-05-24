#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
BaseSelecor
+-- SelectSelector
+-- PollSelector
+-- EpollSelector
+-- DevpollSelector
+-- KqueueSelector
"""

import selectors
import socket
import functools
import logging


logging.basicConfig(level=logging.DEBUG, format="%(asctime)s : %(funcName)s %(message)s")
log = logging.getLogger(__name__)

"""
The echo server example below uses the application data in the SelectorKey to register a callback function to
be invoked on the new event. The main loop gets the callback from the key and passes the socket and event
mask to it. As the server starts, it registers the accept() function to be called for read events on the
main server socket. Accepting the connection produces a new socket, which is then registered with the
read() function as a callback for read events.
"""

class LazyEchoServer(object):

    def __init__(self, address, family=socket.AF_INET, socktype=socket.SOCK_STREAM):
        # super(LazyEchoServer, self).__init__()

        self.address = address
        self.family = family
        self.socktype = socktype
        self.buffersize = 1024
        self.sock = None

        self.selector = selectors.DefaultSelector()
        self.is_running = True

    def __enter__(self):
        self.sock = socket.socket(self.family, self.socktype)
        self.sock.setblocking(False)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(address)
        self.sock.listen(5)
        return self

    def __exit__(self, *exc):
        self.selector.close()

    def serve_forever(self):
        self.selector.register(self.sock, selectors.EVENT_READ, self.accept)

        while self.is_running:
            log.debug('waiting for I/O')
            for key, mask in self.selector.select(timeout=1):
                callback = key.data
                callback(key.fileobj, mask)

        log.info('shutting down')

    def accept(self, sock, mask):
        new_connection, addr = self.sock.accept()
        new_connection.setblocking(False)
        self.selector.register(new_connection, selectors.EVENT_READ, self.read)

    def read(self, connection, mask):
        client_address = connection.getpeername()
        log.debug('read({})'.format(client_address))

        data = connection.recv(self.buffersize)

        if data:
            connection.sendall(data)
        else:
            self.selector.unregister(connection)
            connection.close()
            self.is_running = False


if __name__ == '__main__':
    address = ('localhost', 10000)

    with LazyEchoServer(address) as server:
        server.serve_forever()


## References

# https://pymotw.com/3/selectors/index.html#module-selectors