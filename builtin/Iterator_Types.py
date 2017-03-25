#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python supports a concept of iteration over containers. This is implemented
using two distinct methods; these are used to allow user-defined classes to
support iteration. Sequences, described below in more detail, always support
the iteration methods.

The interator objects themselves are required to support the following two
methods, which together from the iterator protocol.

iterator.__iter__()

    Return the iterator object itself. This is required to allow both containers
    and iterators to be used with the for and in statements. This method
    corresponds to the tp_iter slot of the type structure for Python objects in
    the Python/C API.

iterator.__next__()

    Return the next item from the container. If there are no further items, raise
    the StopIteration exception. This method corresponds to the the tp_iternext
    slot of the type structure for Python objects in the Python/C API.
"""

"""
Generator Types

Python's generators provide a convenient way to implement the iterator procotol.
If a container object's __iter__() method is implemented as a generator, it will
automatically return an iterator object (technically, a generator object)
supplying the __iter__() and __next__() methods. More information about generators
can be found in the documentation for the yield expression.
"""


class ReadFile(object):
    def __init__(self, filename):
        self.obj = open(filename)

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj.__next__()

t = ReadFile('/etc/passwd')
for _ in t:
    print(_)
