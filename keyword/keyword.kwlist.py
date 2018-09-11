#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
keyword.kwlist

Sequence containing all the keywords defined for the interpreter. If any
keywords are defined to only be active when particular __future__ statements
are in effect, these will be included as well.
"""

import keyword


def keyword_kwlist():
    print(keyword.kwlist)

    # ['False',
    #  'None',
    #  'True',
    #  'and',
    #  'as',
    #  'assert',
    #  'break',
    #  'class',
    #  'continue',
    #  'def',
    #  'del',
    #  'elif',
    #  'else',
    #  'except',
    #  'finally',
    #  'for',
    #  'from',
    #  'global',
    #  'if',
    #  'import',
    #  'in',
    #  'is',
    #  'lambda',
    #  'nonlocal',
    #  'not',
    #  'or',
    #  'pass',
    #  'raise',
    #  'return',
    #  'try',
    #  'while',
    #  'with',
    #  'yield']


if __name__ == '__main__':
    keyword_kwlist()

# reference
# https://docs.python.org/3/library/keyword.html#keyword.iskeyword