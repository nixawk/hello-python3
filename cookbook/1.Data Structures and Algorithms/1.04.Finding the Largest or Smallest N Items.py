#!/usr/bin/python
# -*- coding: utf-8 -*-

# Problem

# You want to make a list of the largest or smallest N items in a collection.

# Solution

# The heapq module has two functions nlargest() and nsmallest() that do exactly
# what you want.

import heapq

# heaqp.heappush(heap, item)
# heapq.heappop(heap)
# heapq.heappushpop(heap, item)
# heapq.heapify(x)
# heapq.heapreplace(heap, item)
# heapq.merge(*)


def heapq_functions(iterator):

    # The heapq module provides an implementation of the heap queue algorithm,
    # also known as the priority queue algorithm.

    heap = list(iterator)
    heapq.heapify(heap)
    smallest_value = heapq.heappop(heap)  # Pop and return the smallest item
    heapq.heappush(heap, smallest_value)  # Push the value item onto the heap

    print(heap)


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# Return a list with the n largest elements from the dataset defined by
# iterable. key, if provided, specifies a function of one argument
# that is used to extract a comparison key from each element in the
# iterable: key=str.lower Equivalent to:
# sorted(iterable, key=key, reverse=True)[:n]

print(heapq.nlargest(3, nums))

# Return a list with the n smallest elements from the dataset defined
# by iterable. key, if provided, specifies a function of one argument
# that is used to extract a comparison key from each element in the
# iterable: key=str.lower Equivalent to: sorted(iterable, key=key)[:n]

print(heapq.nsmallest(3, nums))

# Other heapq functions

heapq_functions(nums)

# Discussion

# If you are looking for the N smallest or largest items and N is small
# compared to the overall size of the collection, these functions provide
# superior performance.


# https://docs.python.org/3/library/heapq.html