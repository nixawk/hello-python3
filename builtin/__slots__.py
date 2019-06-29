#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __slots__ allow us to explicitly declare data members (like properties) and
# deny the creation of __dict__ and __weakref__ (unless explicitly declared in
# __slots__ or available in a parent.)

import sys


class MODULE1:

    __slots__ = ["index"]

    def __init__(self, index):
        self.index = index


class MODULE2:

    def __init__(self, index):
        self.index = index

if __name__ == '__main__':
    print("   with __slots__: %d" % sys.getsizeof(MODULE1(111)))
    print("without __slots__: %d" % sys.getsizeof(MODULE2(222)))


"""
$ py2 __slots__.py
   with __slots__: 72
without __slots__: 72

$ python3 __slots__.py
   with __slots__: 48
without __slots__: 56
"""

# references
# https://stackoverflow.com/questions/472000/usage-of-slots
# https://docs.python.org/3/reference/datamodel.html#slots
# http://tech.oyster.com/save-ram-with-python-slots/
