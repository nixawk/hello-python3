#!/usr/bin/python3
# -*- coding: utf-8 -*-

from collections import deque

demo = deque(maxlen=3)
for i in range(10):
    demo.append(i)
print(demo)

demo = [1, 2, 3, 4]
print(deque(demo, maxlen=2))  # return last 2 items
