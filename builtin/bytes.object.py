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

def bytes_object():
    print(bytes([1, 2, 3, 4]))                          # b'\x01\x02\x03\x04'
    print(bytes("hello россия", encoding="utf-8"))      # b'hello \xd1\x80\xd0\xbe\xd1\x81\xd1\x81\xd0\xb8\xd1\x8f'
    print(bytes([0x50, 0x79, 0x74, 0x68, 0x6F, 0x6E]))  # b'Python'
    print(bytes(4))                                     # b'\x00\x00\x00\x00'


if __name__ == '__main__':
    bytes_object()

# references
# https://docs.python.org/3.7/library/stdtypes.html#bytes
# https://docs.python.org/3.7/library/stdtypes.html#bytearray-objects
