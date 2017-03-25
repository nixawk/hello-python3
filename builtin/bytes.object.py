#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
Since bytes objects are sequences of integers (akin to a tuple), for a bytes
object b, b[0] will be an integer, while b[0:1] will be a bytes object of
length 1.
(This contrasts with text strings, where both indexing and slicing will
produce a string of length 1).


bytes(iterable_of_ints) -> bytes
bytes(string, encoding[, errors]) -> bytes
bytes(bytes_or_buffer) -> immutable copy of bytes_or_buffer
bytes(int) -> bytes object of size given by the parameter initialized with null bytes
bytes() -> empty bytes object

Construct an immutable array of bytes from:
  - an iterable yielding integers in range(256)
  - a text string encoded using the specified encoding
  - any object implementing the buffer API.
  - an integer

"""

s = bytes('ß', 'utf-8')
print(s.decode('utf-8'))

print(bytes([0x50, 0x79, 0x74, 0x68, 0x6F, 0x6E]))

print(bytes(4))  # 4 bytes 00 00 00 00
