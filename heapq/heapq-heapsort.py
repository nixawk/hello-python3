#!/usr/bin/python3
# -*- coding: utf-8 -*-

# https://docs.python.org/3/library/heapq.html

import heapq


# This is similar to sorted(iterable), but unlike sorted(),
# this implementation is not stable.
# Heap elements can be tuples. This is useful for assigning comparson values
# (such as task priorities) alongside the main record being tracked.

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print(heapsort(lst))

    lst = [(2, 'cpp'), (1, 'c'), (3, 'python')]
    print(heapsort(lst))
