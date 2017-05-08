#!/usr/bin/python
# -*- coding: utf-8 -*-


from functools import wraps


def decorator(func):
    print('decorator one')
    @wraps(func)
    def wrapper(*args, **kwds):
        return func(*args, **kwds)
    return wrapper


@decorator
def hello():
    print('hello python')


if __name__ == '__main__':
    a = hello
    a()

    print('--------------')

    b = hello.__wrapped__
    b()


"""
decorator one
hello python
--------------
hello python
"""