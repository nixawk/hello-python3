#!/usr/bin/python
# -*- coding: utf-8 -*-

import ctypes


"""
ctypes.cast(obj, type)

This function is similar to the cast operator in C. It returns a new instance of
type which points to the same memory block as obj. type must be a pointer type,
and obj must be an object that can be interpreted as a pointer.
"""

var = ctypes.c_ubyte(0x54)
pointer = ctypes.byref(var, 0)
print(pointer)
print(ctypes.cast(pointer, ctypes.POINTER(ctypes.c_ulong)))
