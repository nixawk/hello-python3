#!/usr/bin/python
# -*- coding: utf-8 -*-

from ctypes import *


"""
ctypes.create_string_buffer(init_or_size, size=None)

    This function creates a mutable character buffer. The returned object is a
    ctypes array of c_char.

    init_or_size must be an integer which specifics the size of the array, or a
    bytes object which will be used to initialize the array items.

    If a bytes object is specified as first argument, the buffer is made one
    item larger than its length so that the last element in the array is a NUL
    termination character. An integer can be passed as second argument which
    allows specifying the size of the array if the length of the bytes should
    not be used.

ctypes.create_unicode_buffer(init_or_size, size=None)

    ...

"""


# create a 3 byte buffer, initialized to NUL bytes
p = create_string_buffer(3)
print(sizeof(p), repr(p.raw))

# create a buffer containing a NUL terminated string
p = create_string_buffer(b'Hello')
print(sizeof(p), repr(p.raw))

# create a 10 byte buffer
p = create_string_buffer(b'Hello', 10)
print(sizeof(p), repr(p.raw))
