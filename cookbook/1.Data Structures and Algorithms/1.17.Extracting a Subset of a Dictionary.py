#!/usr/bin/python
# -*- coding: utf-8 -*-

# Problem

# You want to make a dictionary that is a subset of another dictionary.

# Solution

# This is easily accomplished using a dictionary comprehension.

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Make a dictionary of all prices over 200
p1 = {key: value for key, value in prices.items() if value > 200}

# Discussion

# Much of what can be accomplished with a dictionary comprehension might
# also be done by creating a sequence of tuples and passing them to
# the dict() function.

p2 = dict((key, value) for key, value in prices.items() if value > 200)

print(p1 == p2)
