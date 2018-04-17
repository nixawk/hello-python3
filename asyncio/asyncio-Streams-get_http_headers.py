#!/usr/bin/python
# -*- coding: utf-8 -*-

import asyncio
import urllib.parse
import sys


async def print_http_headers(url):
    url = urllib.parse.urlsplit(url)
    if url.scheme == 'https':
        connect = asyncio.open_connection(url.hostname, 443, ssl=True)
    else:
        connect = asyncio.open_connection(url.hostname, 80)
    reader, writer = await connect
    query = (
        'HEAD {path} HTTP/1.0\r\n'
        'Host: {hostname}\r\n'
        '\r\n'.format(path=url.path or '/', hostname=url.hostname)
    )
    writer.write(query.encode('latin-1'))
    while True:
        line = await reader.readline()
        if not line:
            break
        line = line.decode('latin-1').rstrip()
        if line:
            print('HTTP header> %s' % line)

    # Ignore the body, close the socket
    writer.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('[*] Usage: python %s url' % sys.argv[0])
        sys.exit(0)

    url = sys.argv[1]
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(print_http_headers(url))
    loop.run_until_complete(task)
    loop.close()


# https://docs.python.org/3/library/asyncio-stream.html