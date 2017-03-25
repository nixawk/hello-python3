#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
classmethod bytes.fromhex(string)

This bytes class method returns a bytes object, decoding the given string object.
The string must contain two hexadecimal digits per byte, with ASCII spaces being
ignored.
"""

s1 = '507974686F6E'
s2 = '50 79 74 68 6F 6E'

print(bytes.fromhex(s1))
print(bytes.fromhex(s2))
