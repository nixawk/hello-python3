#!/usr/bin/python
# -*- coding: utf-8 -*-

import ctypes


"""
ctypes.byref(obj[, offset])

Returns a light-weight pointer to obj, which must be an instance of a ctypes type.
offset defaults to zero, and must be an integer that will be added to the internal
pointer value.

byref(obj, offset) corresponds to this C code.

(((char *)&obj) + offset)

The returned object can only be used as a foreign function call parameter. It
behaves similar to pointer(obj), but the construction is a lot faster.
"""

var = ctypes.c_uint32(0x54)
print(ctypes.byref(var, 0))
