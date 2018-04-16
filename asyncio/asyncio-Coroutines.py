#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import datetime


# Coroutines used with asyncio may be implemented using the async def statement,
# or by using generators. The async def type of coroutine was added in Python3.5
# , and is recommended if there is no need to support older Python versions.

# Generator-based coroutines should be decorated with @asyncio.coroutine,
# althrough this is not strictly enforced. The decorator enables compatibility
# with async def corountines, and also serves as documentation. Generator-based
# corontines use the yield from syntax introduced in PEP 380, instead of the
# original yield syntax.

    # @asyncio.coroutine
    # async def

async def hello_world():
    print("Hello World !")


async def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    loop.run_until_complete(hello_world())
    loop.run_until_complete(display_date(loop))

    print('---- different ----')

    loop.run_until_complete(
        asyncio.gather(
            hello_world(),
            display_date(loop)
        )
    )

    loop.close()


# https://docs.python.org/3/library/asyncio-task.html