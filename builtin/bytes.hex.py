#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
bytes.hex()

Return a string object containing two hexadecimal digits for each byte in the
instance.

"""

def bytes_hex():
    data = [
        'Hello Python',
        u'Hello россия',
    ]

    for _ in data:
        print(bytes.hex(_.encode()))

    # import binascii
    # binascii.hexilify(hexstr)


if __name__ == '__main__':
    bytes_hex()


# references
# https://docs.python.org/3.7/library/stdtypes.html#bytes.hex