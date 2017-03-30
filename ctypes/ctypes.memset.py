#!/usr/bin/python
# -*- coding: utf-8 -*-

import ctypes


"""
ctypes.memset(dst, c, count)

    Same as the standard C memset library function: fills the memory block at
    address dst with count bytes of value c.dst must be an integer specifying
    an address, or a ctypes instance.
"""

var = ctypes.c_ubyte(0x54)
ret = ctypes.memset(ctypes.byref(var), 0x55, 4)
print(var.value)
print(ret)
