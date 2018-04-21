#!/usr/bin/python
# -*- coding: utf-8 -*-

# In this section, we describe a classic recursive algorithm, binary search,
# that is used to efficiently locate a target value within a sorted sequence
# of n elements. This is among the most important of computer algorithms,
# and it is the reason that we so often store data in sorted data in sorted
# order.

# When the sequence is unsorted, the standard approach to search for a target
# value is to use a loop to examine every element, until either finding the
# target or exhausting the data set. This is known as the sequential search
# algorithm. This algorithm runs in O(n) time (i.e., linear time) since every
# element is inspected in the worst case.

# When the sequemce is sorted and indexable, there is a much more efficient
# algorithm.

    # mid = (low + high)/2 

# We consider three cases:

    # If the target equals data[mid], then we have found the item we are
    # looking for, and the search terminates successfully.

    # If target < data[mid], then we recur on the first half of the sequence,
    # that is, on the interval of indices from low to mid -1.

    # If target > data[mid], then we recur on the second half of the sequence,
    # that is, on the interval of indices from mid + 1 to high.

# An unsuccessful search occurs if low > high, as the interval [low, high] is
# empty.

def binary_search(data, target, low, high):
    if low > high:
        return Falsse

    mid = (low + high) // 2
    if target == data[mid]:
        print(mid, data[mid], sep=', ')
        return True
    elif target < data[mid]:
        return binary_search(data, target, low, mid - 1)
    else:
        return binary_search(data, target, mid + 1, high)


if __name__ == '__main__':
    seq = ['asm', 'c', 'cpp', 'perl', 'python', 'ruby', 'go', 'shell', 'rust']
    binary_search(seq, 'python', 0, len(seq))
