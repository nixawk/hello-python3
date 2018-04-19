#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import ChainMap

# Problem

# You have multiple dictionaries or mappings that you want to logically combine
# into a single mapping to perform certain operations, such as looking as
# looking up values or checking for the existence of keys.

# Solution

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# Now suppose you want to perform lookups where you have to check both
# dictionaries. An easy way to do this is to use the ChainMap class
# from collections module.

c = ChainMap(a, b)
print(c)
print(c['x'])  # output: 1 
print(c['y'])  # output: 2 
print(c['z'])  # output: 3

# A ChainMap takes multiple mappings and makes them logically appear as one.
# However, the mappings are not literally merged together. Instead, a ChainMap
# simply keeps a list of the underlying mappings and redefines common dictionary
# operations to scan the list.

