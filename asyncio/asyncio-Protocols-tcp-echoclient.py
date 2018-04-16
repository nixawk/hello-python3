#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio


# asyncio provides base classes that you subclass to implement your
# network protocols. Those classes are used in conjuntion with transports
# (see below): the protocol parses incoming data and asks for the writing
# of outgoing data, while the transport is responsible for the actual
# I/O and buffering.

# Protocol classes

    # class asyncio.Protocol
    # class asyncio.DatagramProtocol
    # class asyncio.SubprocessProtocol

# Streaming protocols

    # Protocol.data_received(data)

        # Called when some data is received. data is a non-empty bytes
        # object containing the incoming data.

    # Protocol.eof_received()

        # Called when the other end signals it won't send any more data
        # (for example by calling write_eof(), if the other end also uses
        # asyncio)


    # State machine:

        # 1. start
        # 2. connection_made()
        # 3. data_receibed()
        # 4. eof_received()
        # 5. connection_lost()
        # 6. end

class EchoClientProtocol(asyncio.Protocol):

    def __init__(self, message, loop):
        self.message = message
        self.loop = loop

    def connection_made(self, transport):
        transport.write(self.message.encode())
        print('Date sent: {!r}'.format(self.message))

    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    message = 'Hello, World !'
    client = loop.create_connection(
        lambda: EchoClientProtocol(message, loop),
        '127.0.0.1', 8888
    )

    loop.run_until_complete(client)
    loop.close()


# https://docs.python.org/3/library/asyncio-protocol.html#protocols