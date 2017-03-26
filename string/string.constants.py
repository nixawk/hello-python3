#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
string.ascii_letters

    The concatenation of the ascii_lowercase and ascii_uppercase constants
    described below. This value is not locale-dependent.

string.ascii_lowercase

    The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not
    locale-dependent and will not change.

string.ascii_uppercase

    The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not
    locale-dependent and will not change.

string.digits

    The string '0123456789'

string.hexdigits

    The string '0123456789abcdefABCDEF'

string.octdigits

    The string '01234567'

string.punctuation

    String of ASCII characters which are considered punctuation characters
    in the C local

string.whitespace

    A string containing all ASCII characters that are considered whitespace.
    This includes the characters space, tab, linefeed, return, formfeed, and
    vertical tab.
"""

import string


print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
print(string.octdigits)
print(string.punctuation)
print(string.printable)
print(string.whitespace)
