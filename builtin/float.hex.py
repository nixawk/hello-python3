#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
float.hex()

Return a representation of a floating-point number as a hexadceimal
string. For finite floating-point numbers, this representation will
always include a leading 0x and a trailing p and exponent.

classmethod float.fromhex(s)
Class method to return the float represented by a hexadecimal string
s. The string s may have leading and trailing whitespace.

A hexadecimal string takes the form:

    [sign] ['0x'] integer ['.' fraction] ['p' exponent]

"""

print((2.0).hex())  # 0x1.0000000000000p+1
print((3.1).hex())  # 0x1.8cccccccccccdp+1

print(float.fromhex('0x3.a7p10'))
print(float.fromhex('0x1.8cccccccccccdp+1'))

# references
# https://docs.python.org/3.7/library/stdtypes.html#additional-methods-on-float