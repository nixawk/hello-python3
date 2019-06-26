#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import random
import asyncio


async def part1(n: int) -> int:
    i = random.randint(0, 5)
    print(f"part1: sleeping for {i} seconds.")
    await asyncio.sleep(i)
    return i + n


async def part2(n: int) -> int:
    i = random.randint(0, 5)
    print(f"part2: sleeping for {i} seconds.")
    await asyncio.sleep(i)
    return i + n


async def chain(n: int) -> None:
    start = time.perf_counter()

    # A key feature of coroutines is that they can chained together.
    p1 = await part1(n)
    p2 = await part2(p1)

    end = time.perf_counter() - start
    print(f"--> result: {p1}, cost: {end:0.2f} seconds")


async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))


if __name__ == '__main__':
    args = [0, 1, 2, 3, 4]
    asyncio.run(main(*args))


# references
# https://realpython.com/async-io-python/