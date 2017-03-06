#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import OrderedDict
import json


# OrderedDict - dict subclass that remembers the order entries were added.
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

for key in d:
    print(key, d[key])

print(json.dumps(d))
