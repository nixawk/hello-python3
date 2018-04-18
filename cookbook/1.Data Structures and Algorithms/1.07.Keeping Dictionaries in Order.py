#!/usr/bin/python
# -*- coding: utf-8 -*-


# Problem

# You want to create a dictionary, and you also want to control the order
# of items when iterating or serializing.

# Solution

# To control the order of item in a dictionary. you can use an OrderedDict
# from the collections module. It exactly preserves the original insertion
# order of data when iterating.

from collections import OrderedDict


pairs = {
    'd': 'hello d',
    'b': 'hello b',
    'c': 'hello c',
    'a': 'hello a'
}

# An OrderedDict can be particularly useful when you want to build a
# mapping that you may want to later serialize or encode into a
# different format. 

d = OrderedDict()  # keep key sort order
for key, value in pairs.items():
    d[key] = value

print(d)

# Discussion

# An OrderedDict internally maintains a doubly linked list that orders
# the keys according to insertion order. When a new is first inserted,
# it is placed at the end of this list. Subsequent reassignment of
# an existing key doesn't change the order.

# Be aware that the size of an OrderedDict is more than twice as large
# as a normal dictionary due to the extra linked list that's created.
# Thus, if you are going to build a data structure involving a large
# number of OrderedDict instances, you would need to study the requi
# -rements of your application to determine if the benefits of using
# an OrderedDict outweighted the extra memory overhead.
