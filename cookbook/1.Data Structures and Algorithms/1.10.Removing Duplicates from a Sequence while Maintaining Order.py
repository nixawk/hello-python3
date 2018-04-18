#!/usr/bin/python
# -*- coding: utf-8 -*-

# Problem

# You want to eliminate the duplicate values in a sequence, but preserve the
# order of the remaining items.

# Solution

# If the values in the sequence are hashable, the problem can be easily
# solved using a set and a generator.


def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 3, 1, 9, 1, 5, 10]
print(list(dedupe(a)))


# This only works if the items in the sequence are hashable. If you are
# trying to eliminate duplicates in a sequence of unhashable types (such
# as dicts), you can make a slight change to this recipe.

def dedupe(items, key=None):
    seen = set()
    for item in items:
        # The specification of a key function mimics similar functionality
        # in built-in functions such as sorted().min(), and max()..
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
print(list(dedupe(a, key=lambda d: d['x'])))

## Discussion

# If all you want to do is eliminate duplicates, it is often easy enough to
# make a set.

def set_func():
    a = [1, 2, 3]
    b = [2, 3, 4]

    # TypeError: unsupported operand type(s) for +: 'set' and 'set'
    # print(set(a) + set(b))

    print(set(a) - set(b))
    print(set(b) - set(a))
    print(set(a) | set(b))
    print(set(a) & set(b))


set_func()
