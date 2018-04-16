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


class EchoServerProtocol(asyncio.Protocol):

    def __init__(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}'.format(message))

        print('Send: {!r}'.format(message))
        self.transport.write(data)

        print('Close the client socket')
        self.transport.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    coro = loop.create_server(
        EchoServerProtocol,
        '127.0.0.1', 8888
    )

    server = loop.run_until_complete(coro)

    # Serve requests until Ctrl+C is pressed
    print('Serving on {}'.format(server.sockets[0].getsockname()))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    # Close the server
    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


# https://docs.python.org/3/library/asyncio-protocol.html#protocols