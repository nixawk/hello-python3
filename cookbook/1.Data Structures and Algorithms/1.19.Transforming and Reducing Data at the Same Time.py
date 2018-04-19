#!/usr/bin/python
# -*- coding: utf-8 -*-

# Probem

# You need to execute a reduction function, but first need to transform or
# filter the data.

# Solution

# A very elegant way to combine a data reduction and a transformation is to
# use a generator-expression argument.


nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)

print(s)

# Discussion

# The solution shows a subtle syntatic aspect of generator expressions when
# supplied as the single argument to a function.

# Using a generator argument is often a more efficient and elegant approach
# than first creating a temporary list.

# For example, these statements are the same:

s = sum((x * x for x in nums))
s = sum(x * x for x in nums)
