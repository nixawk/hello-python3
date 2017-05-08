#!/usr/bin/python
# -*- coding: utf-8 -*-

import types
from functools import wraps


class DecoratorClass(object):
	def __init__(self, func):
		wraps(func)(self)
		self.ncalls = 0

	def __call__(self, *args, **kwargs):
		self.ncalls += 1
		return self.__wrapped__(*args, **kwargs)

	def __get__(self, instance, cls):
		if instance is None:
			return self
		else:
			return types.MethodType(self, instance)


@DecoratorClass
def add(x, y):
	return x + y


class Spam:
	@DecoratorClass
	def bar(self, x):
		print(self, x)