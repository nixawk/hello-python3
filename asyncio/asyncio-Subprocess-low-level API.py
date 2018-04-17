#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import sys

# Create a subprocess: low-level API using Process

# loop.subprocess_exec
# loop.subprocess_shell

class Protocol_Factory(asyncio.SubprocessProtocol):

    def __init__(self, exit_future):
        self.exit_future = exit_future
        self.output = bytearray()

    def pipe_data_received(self, fd, data):
        self.output.extend(data)

    def process_exited(self):
        self.exit_future.set_result(True)


async def get_date(loop):
    code = 'import datetime; print(datetime.datetime.now())'
    # exit_future = asyncio.Future(loop=loop)
    exit_future = loop.create_future()

    # Create the subprocess controlled by the protocol Protocol_Factory,
    # redirect the standard output into a pipe.
    create = loop.subprocess_exec(
        lambda: Protocol_Factory(exit_future),
        sys.executable, '-c', code,
        stdin=None, stderr=None
    )

    transport, protocol = await create

    # Wait for the subprocess exit using the process_exited() method
    # of the protocol.
    await exit_future

    # Close the stdout pipe
    transport.close()

    # Read the output which was conllected by the pipe_data_received()
    # method of the protocol.
    data = bytes(protocol.output)
    return data.decode('ascii').rstrip()


if __name__ == '__main__':
    if sys.platform == "win32":
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)
    else:
        loop = asyncio.get_event_loop()

    date = loop.run_until_complete(get_date(loop))
    print("Current ate: %s" % date)
    loop.close()


# https://docs.python.org/3/library/asyncio-subprocess.html