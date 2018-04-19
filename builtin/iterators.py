#!/usr/bin/python
# -*- coding: utf-8 -*-

# Iterators

# There are many types of objects in Python that qualify as being iterable.
# Basic container types, such as list, tuple, and set, qualify as iterable
# types. Furthermore, a string can produce an iteration of its characters,
# a dictionary can produce an iteration of its keys, and a file can produce
# an iteration of its lines. User defined types may also support iteration.
# In Python, the mechanism for iteration is based upon the following
# convrntions:

    # An iterator is an object that manages an iteration through
    # a series of values. If variable, identifiers an iterator
    # object, then each call to the built-in function, next(i),
    # produces a subsequent element from the underlying series,
    # with a StopIteration exception raised to indicate that
    # there are no further elements.

    # An iterable is an object, that produces an iterator via
    # the syntax iter(obj)

# Python supports a concept of iteration over containers. This is implemented
# using two distinct methods; these are used to allow user-defined classes to
# support iteration. Sequences, described below in more detail, always support
# the iteration methods.

# The interator objects themselves are required to support the following two
# methods, which together from the iterator protocol.

# iterator.__iter__()

#     Return the iterator object itself. This is required to allow both
#     containers and iterators to be used with the for and in statements.
#     This method corresponds to the tp_iter slot of the type structure
#     for Python objects in the Python/C API.

# iterator.__next__()

#     Return the next item from the container. If there are no further items,
#     raise the StopIteration exception. This method corresponds to the the
#     tp_iternext slot of the type structure for Python objects in the
#      Python/C API.


class MyIterator:

    def __init__(self, value):
        self.index = 0
        self.value = value

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.value):
            result = self.value[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration 


MY_LIST = [0, 1, 2, 3, 4]
MY_ITER = MyIterator(MY_LIST)

print(next(MY_ITER))
print(next(MY_ITER))
print(next(MY_ITER))
print(next(MY_ITER))
print(next(MY_ITER))
print(next(MY_ITER))  #  raise StopIteration

# https://wiki.python.org/moin/Iterator
# https://www.programiz.com/python-programming/iterator 