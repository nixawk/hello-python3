#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import sys


# On Windows, the default event loop is SelectorEventLoop which does not
# support subprocesses. ProactorEventLoop should be instead.

# Create a subprocess: high-level API using Process

# asyncio.create_subprocess_exec
# asyncio.create_subprocess_shell


if __name__ == '__main__':

    loop = asyncio.get_event_loop()

    if sys.platform == "win32":
        loop = asyncio.ProactorEventLoop()
        asyncio.set_event_loop(loop)

    loop.run_until_complete(
        asyncio.gather(
            asyncio.create_subprocess_exec('id'),
            asyncio.create_subprocess_exec('pwd'),
            asyncio.create_subprocess_shell('id')
        )
    )


# https://docs.python.org/3/library/asyncio-subprocess.html