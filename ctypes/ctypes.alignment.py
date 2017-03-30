#!/usr/bin/python
# -*- coding: utf-8 -*-

import ctypes


"""
ctypes.alignment(obj_or_type)

Returns the alignment requirements of a ctypes type. obj_or_type must be a ctypes
type or instance.
"""

var = ctypes.c_uint32(0x54)
print(ctypes.alignment(var))
