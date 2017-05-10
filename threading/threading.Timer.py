#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-10s) %(message)s')


def worker():
	logging.debug('worker running')


# A Timer starts its work after a delay, and can be canceled at any point within that
# delay time period.

t1 = threading.Timer(0.3, worker)
t1.setName('t1')

t2 = threading.Timer(0.3, worker)
t2.setName('t2')

logging.debug('starting timers')
t1.start()
t2.start()

logging.debug('waiting before canceling %s', t2.getName())
time.sleep(0.2)
logging.debug('canceling %s', t2.getName())
t2.cancel()
logging.debug('done')

# t1.join()
# t2.join()