#!/usr/bin/python
# -*- coding: utf-8 -*-

# Comparison Operators

# Data types may define a natural order via the following operators:

    # <    less than
    # <=   less than or equal to
    # >    greater than
    # >=   greater than or equal to

# These operators have expected behavior for numeric types, and are defined
# lexicographically, and case-sensitively, for strings. An exception is
# raised if operands have incomparable types, as with 5 < 'hello'.

INT_A = 1234
INT_B = 1232

if INT_A > INT_B:
    print('INT_A > INT_B')

