#!/usr/bin/python
# -*- coding: utf-8 -*-

## Daemon vs Non-Daemon Threads

# Default, the above example programs have implicitly waited to exit until all threads
# have completed their work. Sometimes programs spawn a thread as daemon that runs
# without blocking the main program from exiting.

# Using daemon threads is useful for services where there may not be an easy way to
# interrupt the thread, or where letting the thread die in the middle of its work
# does not lose or corrupt data (for example, a thread that generates "heart beats"
# for a service monitoring tool). To mark a thread as a daemon, pass [daemon=True]
# when constructing it or call its [set_daemon()] method with True.

# The default is for threads to not be deamons.

import threading
import logging
import time


logging.basicConfig(level=logging.DEBUG, format="%(threadName)s - %(message)s")


def daemon():
	logging.debug('Starting')
	time.sleep(0.2)
	logging.debug('Exiting')


def non_daemon():
	logging.debug('Starting')
	logging.debug('Exiting')


d = threading.Thread(name='daemon', target=daemon, daemon=True)
t = threading.Thread(name='non-daemon', target=non_daemon)

d.start()
t.start()

# output as follow:
# daemon - Starting
# non-daemon - Starting
# non-daemon - Exiting

# The output does not include the 'Exiting' message from the daemon thread, since all of the
# non-daemon threads (including the main thread) exit before the daemon thread wakes up
# from the sleep() call.

# To wait until a daemon thread has completed its work, use the join() method.

d.join(0.1)
logging.debug('d.isAlive() - {}'.format(d.isAlive()))
t.join()

# By default, join() blocks indefinitely. It is possible to pass float value representing the
# number of seconds to wait for the thread to become inactive. If the thread does not complete
# within the timeout period, join() returns anyway.
