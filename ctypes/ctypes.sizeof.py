#!/usr/bin/python
# -*- coding: utf-8 -*-

import ctypes


"""
ctypes.sizeof(obj_or_type)

    Returns the size in bytes of a ctypes type or instance memory buffer. Does
    the same as the C sizeof operator.
"""

var = ctypes.c_uint32(0xFFFFFFFF)
print(ctypes.sizeof(var))

var = ctypes.c_ulong(0xFFFFFFFF)
print(ctypes.sizeof(var))
