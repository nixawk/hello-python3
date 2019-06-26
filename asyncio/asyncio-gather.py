#!/usr/bin/python
# -*- coding: utf-8 -*-

# Example illustrating how to schedule two coroutines to run concurrently.
# They run for ten minutes, during which the first coroutine is scheduled
# to run every second, while the second is scheduled to run every minute.

import random
import asyncio


COLORS = (
    "\033[0;0m",  # 'End'
    "\033[0;30m", # 'Black'
    "\033[0;31m", # 'Red'
    "\033[0;32m", # 'Green' 
    "\033[0;33m", # 'Brown' 
    "\033[0;34m", # 'Blue'
    "\033[0;36m", # 'Cyan'
    "\033[0;35m", # 'Purple'
    "\033[0;37m", # 'Light Gray'
    "\033[1;30m", # 'Dark Gray'
    "\033[1;31m", # 'Light Red'
    "\033[1;32m", # 'Light Green'
    "\033[1;33m", # 'Yellow'
    "\033[1;34m", # 'Light Blue'
    "\033[1;35m", # 'Light Purple'
    "\033[1;36m", # 'Light Cyan'
    "\033[1;37m", # 'White'
)


async def makerandom() -> int:
    coidx = random.randint(1, len(COLORS) - 1)
    color = COLORS[coidx]

    print(color + f"ColorIndex: {coidx:02d}, Message: This is a color string" + COLORS[0])
    await asyncio.sleep(coidx)
    return coidx


async def main():
    res = await asyncio.gather(*(makerandom() for i in range(20)))
    return res


if __name__ == '__main__':
    asyncio.run(main())


# references
# http://asyncio.readthedocs.io/en/latest/hello_clock.html
# http://www.tldp.org/HOWTO/Bash-Prompt-HOWTO/x329.html
