#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
class str(object='')
class str(object=b'', encoding='utf-8', errors='strict')

    Return a string version of object. If object is not provided, returns the
    empty string. Otherwise, the behavior of str() depends on whether encoding
    or errors is given, as follows.

    If neither encoding nor errors is given, str(object) returns object.__str__(),
    which is the "informal" or nicely printable string representation of object.
    For string objects, this is the string itself. If object does not have a
    __str__() method, then str() falls back to returning repr(object).

    If at least one of encoding or errors is given, object should be a bytes-like
    object (e.g. bytes or bytearray). In this case, if object is a bytes (or bytearray)
    object, then str(bytes, encoding, errors) is equivalent to bytes.decode(encoding, errors).
    Otherwise, the bytes object underlying the buffer object is obtained before calling
    bytes.decode().
"""


class MyStr(object):

    def __str__(self):
        return "This is my string."


s = MyStr()
print(str(s))
