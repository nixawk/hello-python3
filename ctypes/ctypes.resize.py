#!/usr/bin/python
# -*- coding: utf-8 -*-

import ctypes


"""
ctypes.resize(obj, size)

    This function resizes the internal memory buffer of obj, which must be an
    instance of a ctypes type. It is not possible to make the buffer smaller
    than the native size of the objects type, as given by sizeof(type(obj)),
    but it is possible to enlarge the buffer.
"""

var = ctypes.c_ubyte(0x54)
ctypes.resize(var, ctypes.sizeof(ctypes.c_uint32))
print(ctypes.sizeof(var))
