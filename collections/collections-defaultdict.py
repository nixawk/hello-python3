#!/usr/bin/python3

from collections import defaultdict


# dict subclass that calls a factory function to supply missing values.
d = defaultdict(list)   # create key automatically
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

print(d)


d = {}    # create key manually
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)

print(d)

d = {}
d.setdefault('a', set()).add(1)
d.setdefault('a', set()).add(2)
d.setdefault('b', set()).add(4)

print(d)
