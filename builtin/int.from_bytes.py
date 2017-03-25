#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
int.from_bytes(bytes, byteorder, *, signed=False)

Return the integer represented by the given array of bytes.

The argument bytes must either be a bytes-like object or iterable producing bytes.

The byteorder argument determines the byte order used to represent the integer.
If byteorder is "big", the most significant byte is at the beginning of the byte
array. If byteorder is "little", the most significant byte is at the end of the
byte array. To request the native byte order of the host system, use sys.byteorder
as the byte order value.
"""

b = b'\x00\x10'
print(int.from_bytes(b, byteorder='big'))
print(int.from_bytes(b, byteorder='little'))
