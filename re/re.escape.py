#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
re.escape(string)

    Escape all the characters in pattern except ASCII letters, numbers and '_'.
    This is useful if you want to match an arbitrary literal string that may
    have regular expression metacharacters in it.
"""

import re

s = '.*\s+'
print(re.escape(s))
