#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
re.match(pattern, string, flags=0)

    If zero or more characters at the beginning of string match the regular
    expression pattern, return a corresponding match object. Return None if
    the string does not  match the pattern; note that this is different from
    a zero-length match.

    Note that even in re.MULTILINE mode, re.match() will only match at the
    beginning of the string and not at the beginning of the each line.

    If you want to locate a match anywhere in string, use search() instead
    (see also search() vs match())
"""

import re


s = '--hello\nworld--'
print(re.match('he', s, re.I))
print(re.search('he', s, re.I))
