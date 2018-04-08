#!/usr/bin/python
# -*- coding: utf-8 -*-

# PEP 515: Underscores in Numeric Literals

# PEP 515 adds the ability to use underscores in numeric literals for improved
# readability.

# grouping decimal numbers by thousands
amount = 10_000_000.0

# grouping hexadecimal addresses by words
addr = 0xCAFE_F00D

# grouping bits into nibbles in a binary literal
flags = 0b_0011_1111_0100_1110

# same, for string conversions
flags = int('0b_1111_0000', 2)

# print result
print(amount)
print(addr)
print(flags)


# References
# https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep515
# https://www.python.org/dev/peps/pep-0515/