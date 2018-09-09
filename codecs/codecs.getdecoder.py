#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
codecs.getdecoder(encoding)

Look up the codec for the given encoding and return its decoder function.
Raises a LookupError in case the encoding cannot be found.
"""

import codecs


def codecs_getdecoder():
    func = codecs.getdecoder('utf-8')    # decode
    print(func.__name__)

    func = codecs.getdecoder('latin-1')  # latin_1_decode
    print(func.__name__)


if __name__ == '__main__':
    codecs_getdecoder()

# reference
# https://docs.python.org/3.7/library/codecs.html#codecs.getencoder