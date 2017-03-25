#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
int.to_bytes(length, byteorder, *, signed=True)

The integer is represented using length bytes. An OverflowError is raised if
the integer is not representable with the given number of bytes.

The byteorder argument determines the byte order used to represent the integer.
If byteorder is "big", the most significant byte is at the beginning of the byte
array. If byteorder is "little", the most significant is at the end of the byte
array. To request the native byte order of the host system, use sys.byteorder
as the byte order value.

The signed argument determines whether two's complement is used to represent the
integer. If signed is False and a negative integer is given, an OverflowError is
raised. The default value for signed is False.
"""

n = 65535

print(n.to_bytes(4, byteorder='big'))
print(n.to_bytes(4, byteorder='big', signed=True))

print(n.to_bytes(4, byteorder='little'))
print(n.to_bytes(4, byteorder='little', signed=True))
