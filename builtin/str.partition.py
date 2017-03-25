#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
str.partition(sep)
str.rpartition(sep)

Split the string at the first occurrence of sep, and return a 3-tuple
containing the part before the separator, the separator itself, and the
part after the separator. If the separator is not found, return a 3-tuple
containing the string itself, followed by two empty strings.
"""

s = "bob@example.com"
print(s.partition('@'))
