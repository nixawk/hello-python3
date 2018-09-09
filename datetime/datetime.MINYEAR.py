#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
datetime.MINYEAR
    The smallest year number allowed in a date or datetime object. MINYEAR is 1.

datetime.MAXYEAR
    The largest year number allowed in a date or datetime object. MAXYEAR is 9999.
"""

import datetime


def datetime_MINYEAR():
    print(datetime.MINYEAR)


def datetime_MAXYEAR():
    print(datetime.MAXYEAR)


if __name__ == '__main__':
    datetime_MINYEAR()
    datetime_MAXYEAR()

# reference
# https://docs.python.org/3/library/datetime.html
