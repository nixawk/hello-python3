#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
classmethod bytes.fromhex(string)

This bytes class method returns a bytes object, decoding the given string object.
The string must contain two hexadecimal digits per byte, with ASCII spaces being
ignored.
"""


def bytes_fromhex():
    data = [
        '507974686F6E',
        '50 79 74686F6E',
        '50 79 74 68 6F 6E'
    ]

    for _ in data:
        print(bytes.fromhex(_))

    # import binascii
    # binascii.unhexilify(s1)
    # binascii.unhexilify(s2)


if __name__ == '__main__':
    bytes_fromhex()


# references
# https://docs.python.org/3.7/library/stdtypes.html#bytes.fromhex
