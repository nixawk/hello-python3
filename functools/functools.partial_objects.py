#!/usr/bin/python
# -*- coding: utf-8 -*-

import functools


## Decorators

# The primary tool supplied by the functools module is the class partial, which can be used to "wrap"
# a callable object with default arguments. The resulting object is itself callable and can be treated
# as though it is the original function. It takes all of the same arguments as the original, and can be
# invoked with extra positional or named arguments as well.

# A partial can be used instead of a lambda to provide default arguments to a function, while leaving
# some arguments unspecified.

class ClassOne(object):
	pass


def foo(a, b=2):
	"""Docstring for foo().
	"""
	print("    called foo with:", (a, b))


if __name__ == '__main__':
	foo2 = functools.partial(foo, b=4)
	foo2("a")

	cls2 = functools.partial(ClassOne)
	setattr(cls2, 'foo', foo)

	cls2.foo('a', b=5)