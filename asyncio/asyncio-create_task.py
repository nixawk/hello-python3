#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio


async def say(what, when):
    await asyncio.sleep(when)
    print(what)


loop = asyncio.get_event_loop()
loop.create_task(say('first hello', 2))
loop.create_task(say('second hello', 1))

# Note that this example will never terminate, as the loop is asked
# to run_forever.
loop.run_forever()
loop.close()


# http://asyncio.readthedocs.io/en/latest/hello_world.html#creating-tasks