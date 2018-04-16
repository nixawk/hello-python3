#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import functools


def greeting(welcome):
    print(welcome)


def say(loop, what):
    print(loop.time(), what)


async def main(loop):
    loop.call_later(3, functools.partial(greeting, "first call"))
    loop.call_later(2, functools.partial(greeting, "second call"))
    loop.call_later(1, functools.partial(say, loop, "third call"))

    await asyncio.sleep(8)  # wait all tasks finished.

# The event loop has its own internal clock for computing timeouts. Which
# clock is used depends on the (platform-specific) event loop implementation;
# ideally it is a monotonic clock. This will generally be a different clock
# than time.time().

# AbstractEventLoop.call_later(delay, callback, *args)
# AbstractEventLoop.call_at(when, callback, *args)
# AbstractEventLoop.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()


# https://docs.python.org/3/library/asyncio-eventloop.html#delayed-calls