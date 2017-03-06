#!/usr/bin/python
# -*- coding: utf-8 -*-

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))
print(max(prices_and_names))   # Python2 runs ok, but python3 fails

"""
Traceback (most recent call last):
  File "zip.py", line 14, in <module>
    print(max(prices_and_names))
ValueError: max() arg is an empty sequence
"""
