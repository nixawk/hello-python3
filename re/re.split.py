#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
re.split(pattern, string, maxsplit=0, flags=0)
    Split string by the occurrences of pattern. If capturing parentheses are
    used in pattern, then the text of all groups in the pattern are also
    returned as part of the resulting list. It maxsplit is nonzero, at most
    maxsplit splits occur, and the remainder of the string is returned as
    the final element of the list.
"""

import re


text = 'c/cpp,python java js'
langs = re.split(r'[/,\s]', text)
print(langs)
