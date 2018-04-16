#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import functools

try:
    from socket import socketpair
except ImportError:
    from asyncio.windows_utils import socketpair


def reader(loop, rsock):
    data = rsock.recv(100)
    print("Received:", data.decode())

    # We are done: unregister the file descriptor
    loop.remove_reader(rsock)

    # Stop the event loop
    loop.stop()


def writer(loop, wsock):
    wsock.send("sent by writer".encode())

    # We are done: unregister the file descriptor
    loop.remove_writer(wsock)

    # Stop the event loop
    # loop.stop()  #  make reader accepts all content.


if __name__ == '__main__':

    # Create a pair of connected file descriptors
    rsock, wsock = socketpair()
    loop = asyncio.get_event_loop()

    # Register the file descriptor for read event
    loop.add_writer(wsock, functools.partial(writer, loop, wsock))
    loop.add_reader(rsock, functools.partial(reader, loop, rsock))

    # Simulate the reception of data from the network
    # loop.call_soon(wsock.send, 'watch a file descriptor'.encode()) # bindara for socket

    # Run the event loop
    loop.run_forever()

    # We are done, close sockets and the event loop
    rsock.close()
    wsock.close()
    loop.close()

# https://docs.python.org/3/library/asyncio-eventloop.html#watch-file-descriptors
# https://docs.python.org/3/library/asyncio-eventloop.html#watch-a-file-descriptor-for-read-events