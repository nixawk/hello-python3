#!/usr/bin/env pyhon3
# -*- coding: utf-8 -*-

"""
concurrent.futures.as_completed(fs, timeout=None)

Returns an iterator over the Future instances (possibly created by different
Executor instances) given by fs that yields futures as they complete (finished
or were cancelled). Any futures given by fs that are duplicated will be
returned once. Any futures that completed before as_completed() is called
will be yielded first. The returned iterator raises a
concurrent.futures.TimeoutError if __next__() is called and the result
isn’t available after timeout seconds from the original call to as_completed().
timeout can be an int or float. If timeout is not specified or None, there is
no limit to the wait time.
"""

from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed
)

import time
import random


def thread_func(i):
    time.sleep(random.randint(1, 4))
    return i


if __name__ == '__main__':
    futures = []
    elements = list(range(10))
    with ThreadPoolExecutor(max_workers=4) as executor:
        for i in elements:
            futures.append(executor.submit(thread_func, i))

    for future in as_completed(futures):
        # future.add_done_callback
        # future.cancel
        # future.cancelled
        # future.done
        # future.exception
        # future.result
        # future.running
        # future.set_exception
        # future.set_result
        # future.set_running_or_notify_cancel
        print(future.result())


# reference
# https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.as_completed
# https://docs.python-guide.org/scenarios/speed/#concurrency