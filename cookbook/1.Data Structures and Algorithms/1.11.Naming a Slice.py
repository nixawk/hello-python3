#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Problem

# Your program has become an unreadable mess of hardcoded slice indices
# and you want to clean it up.

# Solution

# Suppose you have some code that is pulling specific data fields out of
# a record string with fixed fields.

###### 0123456789012345678901234567890123456789012345678901234567890'
record = '....................100          .......513.25          ..........'
cost = int(record[20:32]) * float(record[40:48])

# Instead of doing that, why not name the slices like this?

SHARES = slice(20, 32)
PRICE = slice(40, 48)

print(record[SHARES])
print(record[PRICE])

cost = int(record[SHARES]) * float(record[PRICE])

# In the latter version, you avoid having a lot of mysterious hardcoded
# indices, and waht you're doing becomes much clearer.

# Discussion

# As a general rule, writing code with a lot of hardcoded index values
# leads to a readability and maintenance mess. For example, if you come
# back to the code a year later, you'll look at it and wonder what you
# were thinking when you wrote it. The solution shown is simply a way
# of more clearly stating what your code is actually doing.

# In general, the built-in slice() creates a slice object that can be
# used anywhere a slice is allowed.

# If you have a slice instance s, you can get more information about
# it by looking at its

    # s.start
    # s.stop
    # s.step

def show_slice_attributes():
    items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    s = slice(1, 9, 2)

    print(items[s])
    print(s.start)
    print(s.stop)
    print(s.step)

show_slice_attributes()
