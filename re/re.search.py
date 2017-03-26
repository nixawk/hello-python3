#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
re.search(pattern, string, flags=0)

    Scan through string looking for the first location where the regular
    expression pattern produces a match, and return a corresponding match
    object. Return None if no position in the string matches the pattern;
    note that this is different fron finding a zero-length match at some
    point in the string.
"""

import re


pattern = '^(.*)'
s = 'hello\nworld'

regex = re.compile(pattern)
print(regex.search(s).groups())
