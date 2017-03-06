#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import ChainMap


a1 = {'x': 1, 'y': 2}
b1 = {'y': 3, 'z': 4}

c1 = ChainMap(a1, b1)
d1 = ChainMap(b1, a1)

print(dict(c1))  # {'z': 4, 'y': 2, 'x': 1}
print(dict(d1))  # {'x': 1, 'y': 3, 'z': 4}
