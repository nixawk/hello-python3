#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio


async def say(what, when):
    await asyncio.sleep(when)
    print(what)


async def stop_after(loop, when):
    await asyncio.sleep(when)
    loop.stop()


loop = asyncio.get_event_loop()
loop.create_task(say('first hello', 2))
loop.create_task(say('second hello', 1))
loop.create_task(say('third hello', 4))
loop.create_task(stop_after(loop, 3))

loop.run_forever()
loop.close()


"""
$ py3 asyncio-stop.py
second hello
first hello
Task was destroyed but it is pending!
task: <Task pending coro=<say() done, defined at asyncio-stop.py:7> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x10437b8e8>()]>>
"""