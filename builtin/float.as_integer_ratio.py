#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
float.as_integer_ratio()

Return a pair of integers whose ratio is exactly equal to the original
float and with a positive denominator. Raises OverflowError on infinities
and a Value Error on NaNs. 
"""

print((2.0).as_integer_ratio())  # (2, 1)
print((3.1).as_integer_ratio())  # (6980579422424269, 2251799813685248)

# references
# https://docs.python.org/3.7/library/stdtypes.html#additional-methods-on-float