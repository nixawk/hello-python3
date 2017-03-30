#!/usr/bin/python
# -*- coding: utf-8 -*-

import ctypes


"""
ctypes.addressof(obj)

Returns the address of the memory buffer as integer. obj must be an instance
of a ctypes type.
"""

var = ctypes.c_ubyte(0x54)
print(ctypes.addressof(var))
