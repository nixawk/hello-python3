#!/usr/bin/python
# -*- coding: utf-8 -*-

a1 = {'k1': 'v1', 'k2': 'v2'}
a2 = {'k1': 'v11', 'k2': 'v2', 'k3': 'v3'}

print(a1.keys() & a2.keys())
print(a1.keys() | a2.keys())
print(a1.keys() - a2.keys())
print(a2.keys() - a1.keys())

print(a1.items() & a2.items())

# If python2, it fails
