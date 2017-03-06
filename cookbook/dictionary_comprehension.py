#!/usr/bin/python3
# -*- coding: utf-8 -*-

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# the dictionary comprehension solution is a bit clearer and actually runs
# quite a bit faster
p1 = {key: value for key, value in prices.items() if value > 200}
p2 = dict((key, value) for key, value in prices.items() if value > 200)

print(p1)
print(p2)
