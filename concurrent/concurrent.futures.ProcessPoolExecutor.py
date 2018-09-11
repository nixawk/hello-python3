#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
The ProcessPoolExecutor class is an Executor subclass that uses a pool of
processes to execute calls asynchronously. ProcessPoolExecutor uses the
multiprocessing module, which allows it to side-step the Global Interpreter
Lock but also means that only picklable objects can be executed and returned.

The __main__ module must be importable by worker subprocesses. This means
that ProcessPoolExecutor will not work in the interactive interpreter.

class concurrent.futures.ProcessPoolExecutor(max_workers=None, mp_context=None, initializer=None, initargs=())

An Executor subclass that executes calls asynchronously using a pool of at
most max_workers processes. If max_workers is None or not given, it will
default to the number of processors on the machine. If max_workers is lower
or equal to 0, then a ValueError will be raised. mp_context can be a
multiprocessing context or None. It will be used to launch the workers.
If mp_context is None or not given, the default multiprocessing context is used.

initializer is an optional callable that is called at the start of each worker
process; initargs is a tuple of arguments passed to the initializer. Should
initializer raise an exception, all currently pending jobs will raise a
BrokenThreadPool, as well any attempt to submit more jobs to the pool.
"""

from concurrent.futures import ProcessPoolExecutor
from multiprocessing import cpu_count
import requests


def process_func(url):
    resp = requests.get(url)
    print("%d - %s" % (resp.status_code, url))


def concurrent_futures_ProcessPoolExecutor():
    urls = [
        'https://www.python.org',
        'https://www.google.com',
        'https://www.bing.com',
        'https://www.yahoo.com',
        'https://www.baidu.com',
        'https://www.yandex.com'
    ]
    with ProcessPoolExecutor() as executor:
        executor.map(process_func, urls)


if __name__ == '__main__':
    print("[*] default cpu cout: %d" % cpu_count())
    concurrent_futures_ProcessPoolExecutor()


# reference
# https://docs.python.org/3/library/concurrent.futures.html#processpoolexecutor
# https://stackoverflow.com/questions/1006289/how-to-find-out-the-number-of-cpus-using-python
# https://stackoverflow.com/questions/20776189/concurrent-futures-vs-multiprocessing-in-python-3
# https://docs.python-guide.org/scenarios/speed/#concurrency