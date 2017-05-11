#!/usr/bin/python
# -*- coding: utf-8 -*-

## Controlling Access to Resources

# In addition to synchronizing the operations of threads, it is also important to be
# able to control access to shared resources to prevent corruption or missed data.
# Python's built-in data structures (lists, dictionaries, etc.) are thread-safe as
# a side-effect of having atomic byte-codes for manipulating them (the global interpreter
# lock used to protect Python's internal data structures is not released in the middle 
# of an update). Other data structures implemented in Python, or simpler types like
# integers and floats, do not have that protection. To guard against simultaneous
# access to an object, use a Lock object

import threading
import logging
import random
import time

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')


class Counter(object):

    def __init__(self, start=0):
        self.lock = threading.Lock()
        self.value = start

    def increment(self):
        logging.debug('Waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('Acquired lock')
            self.value += 1
        finally:
            self.lock.release()


def worker(c):
    for i in range(2):
        pause = random.random()
        logging.debug('Sleeping %0.02f', pause)
        time.sleep(pause)
        c.increment()
    logging.debug('Done')


if __name__ == '__main__':
    counter = Counter()
    for i in range(2):
        t = threading.Thread(target=worker, args=(counter,))
        t.start()

    logging.debug('Waiting for worker threads')
    main_thread = threading.main_thread()

    for t in threading.enumerate():
        if t is not main_thread: t.join()

    logging.debug('Counter: %d', counter.value)