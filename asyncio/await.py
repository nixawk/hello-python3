#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The syntax async def introduces either a native coroutine or an asynchronous
generator. The expressions async with and async for are also valid, and you'll
see them later on.


The keyword await passes function control back to the event loop. (it suspends
the execution of the surrounding coroutine.) If python encounters an await f()
expression in the scope of g(), this is how await tells the event loop, "Suspend
execution of g() until whatever I'm waiting on - the result of f() - is returned.
In the meantime, go let something else run."


Rules:

Using await and/or return creates a coroutine function. To call a coroutine
function, you must await it to get its results.

It is less common to use yield in an async def block. This creates an
asynchronous generator, which you iterate over with async for. Forget about
async generators for the time being and focus on getting down the syntax for
coroutine functions, which use await and/or return.

Anything defined with async def may not use yield from, which will raise a
SyntaxError.
"""

import random
import asyncio


async def f():
    await asyncio.sleep(1)
    return random.randint(1, 10)


async def g():
    r = await f()  # pause here and come back to g() when f() is ready
    return r


async def main():
    r = await asyncio.gather(g(), g(), g(), g(), g())
    print(r)


if __name__ == '__main__':
    asyncio.run(main())
