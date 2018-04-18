#!/usr/bin/python
# -*- coding: utf-8 -*-

# Python provides a variety of useful built-in data structures, such as lists
# sets, and dictionaries. For the most part, the use of these structures is
# straightforward. However, common questions concerning searching, sorting,
# ordering, and filtering often arise.

# Problem

# You have an N-element tuple or sequence that you would like to unpack into
# a collection of N variables.

# Solution

# Any sequence (or iterable) can be unpacked into variable using a simple
# assignment operation. The only requirement is that the number of variable
# and structure match the sequence. For example:

p = (4, 5)
x, y = p

print(x, y)


data = ['ACME', 50, 91.1, (2018, 4, 16)]
name, shares, price, date = data

print(name, shares, price, date)

# IF there is a mismatch in the number of elements, you'll get an error.
# For example:

"""
>>> p = (4, 5)
>>> x, y, z = p
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 3, got 2)
"""


# Discussion

# Unpacking actually works with any object that happens to be iterable, not
# just tuples or lists. This includes strings, files, iterators, and generators.
