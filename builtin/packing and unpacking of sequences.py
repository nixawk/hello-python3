#!/usr/bin/python
# -*- coding: utf-8 -*-

# Packing and Unpacking of Sequences

# Python provides two additional conveniences involving the treatment of tuples
# and other sequence types.. The first is rather cosmetic. If a series of
# comma-separated expressions are given in a larger context, they will be
# treated as a single tuple, even if no enclosing parentheses are provided.

data = 1, 2, 3, 4
print(type(data))

# results in identifier, data, being assigned to the tuple (1, 2, 3, 4).
# This behavior is called automatic packing of a tuple. One common use of
# packing in Python is when returning multiple values from a function. If
# the body of a function executes the command.

def automatic_packing(x, y):
    return x, y   # return (x, y)


def automatic_unpacking(pack):
    x, y = pack   # unpack
    return x
