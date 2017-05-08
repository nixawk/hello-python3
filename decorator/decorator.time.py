#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
from functools import wraps


def timethis(func):
	"""Decorator that reports the execution time.
	"""
	@wraps(func)
	def wrapper(*args, **kwds):
		start = time.time()
		result = func(*args, **kwds)
		end = time.time()
		print(func.__name__, end - start)
	return wrapper


@timethis
def countdown(n):
	"""Count down
	"""
	while n > 0:
		n -= 1


if __name__ == '__main__':
	countdown(100000)


# @staticmethod, 
# @classmethod, 
# @property

# http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python