#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
In addition to using Events, another way of synchronizing threads is through using a 
Condition object. Because the Condition uses a Lock, it can be tied to a shared resource,
allowing multiple threads to wait for the resource to be updated. In this example, the
consumer() threads wait for the Condition to be set before continuing. The producer() thread
is responsible for setting the condition and notifying the other threads that they can continue.
"""

import threading
import logging
import time


logging.basicConfig(level=logging.DEBUG, format="%(threadName)s - %(message)s")


def consumer(cond):
	"""wait for the condition and use the resource
	"""
	logging.debug("Starting consumer thread")
	with cond:
		cond.wait()
		logging.debug("Resource is available to consumer")


def producer(cond):
	"""set up the resource to be used by the consumer
	"""
	logging.debug("Starting producer thread")
	with cond:
		logging.debug('Making resource available')
		cond.notifyAll()


if __name__ == '__main__':
	condition = threading.Condition()

	c1 = threading.Thread(name='c1', target=consumer, args=(condition,))
	c2 = threading.Thread(name='c2', target=consumer, args=(condition,))
	p1 = threading.Thread(name='p1', target=producer, args=(condition,))

	c1.start()
	time.sleep(0.2)
	c2.start()
	time.sleep(0.2)
	p1.start()