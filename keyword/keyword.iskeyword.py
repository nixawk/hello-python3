#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
keyword.iskeyword(s)

Return true if s is a Python keyword.
"""

import keyword


def keyword_iskeyword():
    print(keyword.iskeyword("True"))
    print(keyword.iskeyword("lambda"))
    print(keyword.iskeyword("python"))


if __name__ == '__main__':
    keyword_iskeyword()


# reference
# https://docs.python.org/3/library/keyword.html#keyword.iskeyword