#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
codecs.getencoder(encoding)

Look up the codec for the given encoding and return its encoder function.
Raises a LookupError in case the encoding cannot be found.
"""

import codecs


def codecs_getencoder():
    func = codecs.getencoder('utf-8')    # utf_8_encode
    print(func.__name__)

    func = codecs.getencoder('latin-1')  # latin_1_encode
    print(func.__name__)


if __name__ == '__main__':
    codecs_getencoder()

# reference
# https://docs.python.org/3.7/library/codecs.html#codecs.getencoder