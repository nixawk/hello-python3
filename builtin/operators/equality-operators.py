#!/usr/bin/python
# -*- coding: utf-8 -*-

# Equality Operators

# Python supports the following operators to test two notions of equality:

    # is       same identity
    # is not   different identity
    # ==       equivalent
    # !=       not equivalent

INT_A = 1234
INT_B = 1234
INT_C = 123 


if INT_A is INT_B:
    print('INT_A is INT_B', id(INT_A), id(INT_B))

if INT_A is not INT_B:
    print('INT_A is not INT_B', id(INT_A), id(INT_B))

if INT_A == INT_B:
    print('INT_A == INT_B')

if INT_A != INT_C:
    print('INT_A != INT_C')
