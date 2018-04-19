#!/usr/bin/python
# -*- coding: utf-8 -*-

# Instantiation

# The process of creating a new instance of a class is known as instantiation.
# In general, the syntax for instantiating an object is to invoke the
# constructor of a class.

# From a programmer's perspective, yet another way to indirectly create a new
# instance of a class is to call a function that creates and returns such an
# instance. For example, Python has a built-in function named sorted that
# takes a sequence of comparable elements as a parameter and returns a new
# instance of the list class containing those elements in sorted order.

# __init__ is roughly what represents a constructor in Python.

class MyClass:

    def __init__(self):
        print('__init__ is the constructor for a class')

    def __del__(self):
        print('__del__ is the destructor for a class')

    def __enter__(self):
        print('__enter__ is for context manager')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print('__exit__ is for context manager')

    def greeting(self):
        print('hello python')


if __name__ == '__main__':
    with MyClass() as mycls:
        mycls.greeting()


"""
$ python3 class.objects_instantiation.py
__init__ is the constructor for a class
__enter__ is for context manager
hello python
__exit__ is for context manager
__del__ is the destructor for a class
"""

# https://docs.python.org/3/tutorial/classes.html
# https://stackoverflow.com/questions/625083/python-init-and-self-what-do-they-do
# https://stackoverflow.com/questions/865115/how-do-i-correctly-clean-up-a-python-object