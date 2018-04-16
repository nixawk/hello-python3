#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio


# A task is a subclass of Future.
async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        await asyncio.sleep(1)
        f *= i

    print("Task %s: factorial(%s) = %s" % (name, number, f))


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        asyncio.gather(
            factorial("A", 2),
            factorial("B", 3),
            factorial("C", 4),
        )
    )
    loop.close()


# https://docs.python.org/3/library/asyncio-task.html#task