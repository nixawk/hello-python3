#!/usr/bin/python3
# -*- coding: utf-8 -*-

import heapq


nums = [1, 1, 2, 3, 0, 2, 4, 3, 5]
print(heapq.nlargest(4, nums))
print(heapq.nsmallest(4, nums))

iters = [(2, 'cpp'), (1, 'c'), (4, 'Python'), (3, 'Java')]
print(heapq.nlargest(3, iters))
print(heapq.nsmallest(3, iters))

# heapq.nlargest(n, iterable, key=None)
# Find the n largest elements in a dataset

# Equivalent to: sorted(iterable, key=key, reverse=True)


# heapq.nsmallest(n, iterable, key=None)
# Find the n smallest elements in a dataset.

# Equivalent to: sorted(iterable, key=key)
