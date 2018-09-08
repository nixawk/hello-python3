#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
bytes.endswith(suffix[, start[, end]])¶
bytearray.endswith(suffix[, start[, end]])

Return True if the binary data ends with the specified suffix,
otherwise return False. suffix can also be a tuple of suffixes
to look for, With optional start, test begining at that position.
With optional end, stop comparing at that position.

The suffix(es) to search for may be any bytes-like object. 
"""

def bytes_endswith():
    s1 = bytes("helloworld", encoding="utf-8")
    s2 = bytes("world", encoding="utf-8")

    print(s1.endswith(s2))


if __name__ == '__main__':
    bytes_endswith()


# reference
# https://docs.python.org/3.7/library/stdtypes.html#bytes.endswith