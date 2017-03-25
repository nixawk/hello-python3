#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Return the number of bits necessary to represent an integer in binary,
excluding the sign and leading zeros

def bit_length(self):
    s = bin(self)       # binary representation: bin(-37)  --> -0b100101''
    s = s.lstrip('-0b') # remove leading zeros and minus sign
    return len(s)       # len('100101') -> 6

"""

n = 65535
print("[{}] has bit length: {}".format(n, n.bit_length()))   # Python 3
