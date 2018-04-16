#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import functools


def greeting(welcome):  # no async declare here
    print(welcome)


async def main(loop):
    loop.call_soon_threadsafe(functools.partial(greeting, "hello asyncio"))
    loop.call_soon(functools.partial(greeting, "hello asyncio"))

    # Most asyncio functions don't accept keyword. If you want to pass keywords
    # to your callback, use functions.partial(). For example,
    # loop.call_soon(functions.partial(print, "Hello", flush=True))
    # will call print("Hello, flush=True")

    # Note: functools.partial() is better than lambda functions, because
    # asyncio can inspect functions.partial() object to display parameters
    # in debug mode, whereas lambda functions have a poor representation.


loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()


# https://docs.python.org/3/library/asyncio-eventloop.html#calls