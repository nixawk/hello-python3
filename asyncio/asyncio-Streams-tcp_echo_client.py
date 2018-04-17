#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio


async def tcp_echo_client(message, loop):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888, loop=loop
    )

    print('Send: %r' % message)
    writer.write(message.encode())

    data = await reader.read(100)
    print('Received: %r' % data.decode())

    print('Close the socket')
    writer.close()


if __name__ == '__main__':
    message = 'Hello, World!'
    loop = asyncio.get_event_loop()
    loop.run_until_complete(tcp_echo_client(message, loop))
    loop.close()

# https://docs.python.org/3/library/asyncio-stream.html