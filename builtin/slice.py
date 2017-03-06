#!/usr/bin/python
# -*- coding: utf-8 -*-

abc = '1234456789'
print(abc[::2])

sl = slice(None, None, 2)
# print(sl.start)
# print(sl.stop)
# print(sl.step)

for i in range(*sl.indices(len(abc))):
    print(abc[i])
