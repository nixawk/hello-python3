#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
re.findall(pattern, string, flags=0)

Return all non-overlapping matches of pattern in string, as a list of
strings. The string is scanned left-to-right, and matches are returned in
the order found. If one or more groups are present in the pattern, return
a list of groups; this will be a list of tuples if the pattern has more than
one group. Empty matches are included in the result unless they touch the
beginning of another match.
"""


import re


pattern = '<.*?>'
s = '<1> <2> <3> <4>'
regex = re.compile(pattern)
print(regex.findall(s))
