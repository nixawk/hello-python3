#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
str.split(sep=None, maxsplit=-1)

Return a list of the words in the string, using sep as the delimiter string.
If maxsplit is given, at most maxsplit are done (thus, the list will have at
most maxsplit+1 elements). If maxsplit is not specified or -1, then there is
no limit on the number of splits (all possible splits are made).
"""

s = "id,username,password,mail"
print(s.split(','))
print(s.split(',', 1))
