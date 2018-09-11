#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ThreadPoolExecutor is an Executor subclass that uses a pool of threads
to execute calls asynchronously.

Deadlocks can occur when the callable associated with a Future waits on
the results of another Future. 

class concurrent.futures.ThreadPoolExecutor(max_workers=None, thread_name_prefix='', initializer=None, initargs=())

    submit(fn, *args, **kwargs)
    map(func, *iterables, timeout=None, chunksize=1)
"""

from concurrent.futures import ThreadPoolExecutor
import requests


def thread_func(url):
    resp = requests.get(url)
    print("%d - %s" % (resp.status_code, url))


def concurrent_futures_ThreadPoolExecutor():
    urls = [
        'https://www.python.org',
        'https://www.google.com',
        'https://www.bing.com',
        'https://www.yahoo.com',
        'https://www.baidu.com',
        'https://www.yandex.com'
    ]
    with ThreadPoolExecutor(max_workers=2, thread_name_prefix='C') as executor:
        executor.map(thread_func, urls)


if __name__ == '__main__':
    concurrent_futures_ThreadPoolExecutor()


# reference
# https://docs.python.org/3/library/concurrent.futures.html
# https://docs.python-guide.org/scenarios/speed/#concurrency