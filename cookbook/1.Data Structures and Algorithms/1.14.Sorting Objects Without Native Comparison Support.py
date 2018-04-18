#!/usr/bin/python
# -*- coding: utf-8 -*-

# Problem

# You want to sort objects of the same class, but they don't natively support
# comparison operations.

# Solution

# The built-in sorted() function takes a key argument that can be passed a
# callable that will return some value in the object that sorted will use
# to compare the objects.

from operator import itemgetter
from operator import attrgetter


class Item:

    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return 'Item({})'.format(self.value)

    def __getitem__(self, key):  # itemgetter need __getitem__
        # similar to attrgetter
        return getattr(self, key)


items = [Item(5), Item(1), Item(2), Item(3), Item(4)]
print(sorted(items, key=lambda i: i.value))
print(sorted(items, key=itemgetter('value')))
print(sorted(items, key=attrgetter('value')))


# Discussion

# The choice of whether or not to use lambda or attrgetter() may be one of
# personal preference.
