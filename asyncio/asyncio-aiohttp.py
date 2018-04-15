#!/usr/bin/python
# -*- coding: utf-8 -*-

# pip install aiohttp

import asyncio
import aiohttp
import async_timeout


async def fetch_page(session, url):
    async with async_timeout.timeout(10):
        async with session.get(url, ssl=False) as response: # off ssl vertify
            assert response.status == 200
            return await response.read()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, "https://python.org/")
        print(html)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()


# https://aiohttp.readthedocs.io/en/stable/