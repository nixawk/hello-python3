#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio


async def say(what, when):
    await asyncio.sleep(when)
    print(what)


loop = asyncio.get_event_loop()
loop.run_until_complete(say("hello world", 1))
loop.close()

if loop.is_closed():
    print("event loop is closed.")


# https://docs.python.org/3/library/asyncio-eventloop.html
# http://asyncio.readthedocs.io/en/latest/hello_world.html