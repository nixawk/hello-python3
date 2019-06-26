#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Asyncchronous IO (async IO): a language-agnostic paradigm (mode) that has
implementations across a host of programming languages.

async/await: two new Python keywords that are used to define coroutines

asyncio: the Python package that provides a foundation and API for running
and managing coroutines.
"""

import time
import asyncio


async def count():
    print("one")
    await asyncio.sleep(1)
    print("two")


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == '__main__':
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() -s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


# references
# https://realpython.com/async-io-python/
