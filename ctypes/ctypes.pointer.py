#!/usr/bin/python
# -*- coding: utf-8 -*-

import ctypes

"""
ctypes.POINTER(type)

    This factory function creates and returns a new ctypes pointer type. Pointer
    types are cached and reused internally, so calling this function repeatedly
    is cheap. type must be a ctypes type.

ctypes.pointer(obj)

    This function creates a new pointer instance, pointing to obj. The returned
    object is of the type POINTER(type(obj)).

    Note: If you just want to pass a pointer to an object to a foreign function
    call, you should use byref(obj) which is much faster.
"""

var = ctypes.c_ubyte(0x90)
print(ctypes.pointer(var))
print(ctypes.POINTER(ctypes.c_ubyte))
