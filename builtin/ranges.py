#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ranges

The range type represents an immutable sequence of numbers and is
commonly used for looping a specific number of times in for loops.

class range(stop)
class range(start, stop[, step])

    The arguments to the range constructor must be integers
    (either built-in int or any object that implements the
    __index__ special method). If the step argument is
    ommitted, it defaults to 1. The the start argument is
    ommitted, it defaults to 0. If step is zero, ValueError
    is raised.

"""

# for _ in range('A', 'Z'):
#     print(_)

# Traceback (most recent call last):
#   File "ranges.py", line 22, in <module>
#     for _ in range('A', 'Z'):
# TypeError: 'str' object cannot be interpreted as an integer


def split_by_length(string, split_length):
    assert isinstance(string, str)
    for _ in range(0, len(string), split_length):
        yield string[_: _ + split_length]


if __name__ == '__main__':
    string = "AAAABBBBCCCCDDDDEEEEFFFF"
    print(list(split_by_length(string, 4)))
    print(list(split_by_length(string, 8)))


# references
# https://docs.python.org/3.7/library/stdtypes.html#ranges
# https://stackoverflow.com/questions/13673060/split-string-into-strings-by-length