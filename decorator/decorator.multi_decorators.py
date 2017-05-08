#!/usr/bin/python
# -*- coding: utf-8 -*-

from functools import wraps

def decorator_one(func):
    print("decorator_one ----1111----")
    @wraps(func)
    def wrapper(*arg, **kwds):
        print("decorator_one ----3333----")
        func(*arg, **kwds)
    print("decorator_one ----2222----")
    return wrapper


def decorator_two(func):
    print("decorator_two ----AAAA----")
    @wraps(func)
    def wrapper(*arg, **kwds):
        print("decorator_two ----CCCC----")
        func(*arg, **kwds)
    print("decorator_two ----BBBB----")
    return wrapper


@decorator_one
@decorator_two
def hello(name):
    print("hello %s" % name)


if __name__ == '__main__':
    hello('python')
    print(hello)
    print(hello.__wrapped__)  # Not supported: Python 2.x


"""
$ python2.6 decorator.multi_decorators.py
decorator_two ----AAAA----
decorator_two ----BBBB----
decorator_one ----1111----
decorator_one ----2222----
decorator_one ----3333----
decorator_two ----CCCC----
hello python
"""