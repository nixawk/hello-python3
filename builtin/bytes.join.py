#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
bytes.join(iterable)¶
bytearray.join(iterable)

Return a bytes or bytearray object which is the concatenation
of the binary data sequences in iterable. A TypeError will be
raised if there are any values in iterable that are not bytes
-like objects, including str objects. The separator between e
-lements is the contents of the bytes or bytearray object pro
-viding this method.
"""

def bytes_join():

    s1 = 'hello'
    s2 = 'world'

    bytes_data = bytes().join([s1.encode(), s2.encode()])
    print(bytes_data.decode())


if __name__ == '__main__':
    bytes_join()

# reference
# https://docs.python.org/3.7/library/stdtypes.html#bytes.join
