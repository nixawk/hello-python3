#!/usr/bin/python
# -*- coding: utf-8 -*-

# Simultaneous Assignments

# The combination of automatic packing and unpacking forms a technique known
# as simultaneous assignment., whereby we explicitly assign a series of values
# to a series of identifiers, using a syntax:

LIST_A = ['Python', 'C', 'C++', 'ASM', 'Others']
PY, C, CPP, *_ = LIST_A

print(PY)
