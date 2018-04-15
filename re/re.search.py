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


greeting = "hello, world"

result = re.search(r"[aeiou]", greeting)
if result.group():
    print("regex")

if ("a" in greeting
    or "e" in greeting
    or "i" in greeting
    or "o" in greeting
    or "u" in greeting):
    # simlar to re.search
    print("in")


# http://pyvideo.org/pycon-us-2017/readable-regular-expressions.html