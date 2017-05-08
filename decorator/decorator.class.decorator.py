#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
If no functools.wraps, function metainfo will be lost. (func name, func docstring)
"""

from functools import wraps


class A(object):

    # Decorator as an instance method
    def decorator_one(self, func):
        @wraps(func)
        def wrapper(*args, **kwds):
            return func(*args, **kwds)
        return wrapper

    @classmethod
    def decorator_two(cls, func):
        @wraps(func)
        def wrapper(*args, **kwds):
            return func(*args, **kwds)
        return wrapper


class B(A):

    @A.decorator_two
    def hello(self):
        pass


if __name__ == '__main__':
    a = A()

    @a.decorator_one
    def hello_class_instance_decorator():
        pass

    @A.decorator_two
    def hello_class_decorator():
        pass

    hello_class_instance_decorator()
    hello_class_decorator()

# http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python