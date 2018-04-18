#!/usr/bin/python
# -*- coding: utf-8 -*-

# Problem

# You want to make a dictionary that maps keys to more than one value (
# a so-called 'multidict')

# Solution

# A dictionary is a mapping where each key is mapped to a single value.
# If you want to map keys to multiple values, you need to store the
# multiple values in another container such as a list or set.

from collections import defaultdict


d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

e = {
    'a': [1, 2, 3],
    'b': [4, 5]
}

# To easily construct such dictionaries, you can use defaultdict in
# the collections module. A feature of defaultdict is that it
# automatically initializers the first value so you can simply focus
# on adding items.

f = defaultdict(list)
f['a'].append(1)
f['a'].append(2)
f['a'].append(3)
f['b'].append(4)
f['b'].append(5)

# However, many programmers find setdefault() to be a little unnatural
# - not to mention the fact that it always creates a new instance of
# the initial value on each invocation (thhe empty list [] in the example)

g = {}
g.setdefault('a', []).append(1)
g.setdefault('a', []).append(2)
g.setdefault('a', []).append(3)
g.setdefault('b', []).append(4)
g.setdefault('b', []).append(5)


print(d == f)
print(e == g)

# Discussion

# In principle, constructing a multivalued dictionary is simple.
# However, initialization of the first value can be messy if you try
# to do it yourself. For example, you might have code that looks like
# this:

    # d = {}
    # for key, value in pairs:
    #     if key not in d:
    #         d[key] = []
    #     d[key].append(value)

# Using a defaultdict simply leads to much cleaner code:

    # d = defaultdict(list)
    # for key, value in pairs:
    #     d[key].append(value)

def defaultdict_show():
    pairs = {
        'a': 'hello a',
        'b': 'hello b',
        'c': 'hello c'
    }

    items = {
        'a': 'hello aa',
        'b': 'hello bb',
        'c': 'hello cc'
    }

    d = defaultdict(list)
    for key, value in pairs.items():
        print(key,)
        d[key].append(value)

    for key, value in items.items():
        d[key].append(value)

    print(d)
    # defaultdict(<class 'list'>, {
    # 'a': ['hello a', 'hello aa'], 
    # 'b': ['hello b', 'hello bb'], 
    # 'c': ['hello c', 'hello cc']})


defaultdict_show()
