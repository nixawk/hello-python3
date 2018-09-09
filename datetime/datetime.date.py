#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
class datetime.date
    An idealized naive date, assuming the current Gregorian calendar always was,
    and always will be, in effect. Attributes: year, month, and day.
"""

import datetime


def datetime_date():
    # def __new__(cls, year, month=None, day=None):
    date = datetime.date(2018, month=8, day=8)
    print(str(date))     # 2018-08-08
    print(date.ctime())  # Wed Aug  8 00:00:00 2018


if __name__ == '__main__':
    datetime_date()


# reference
# https://docs.python.org/3/library/datetime.html
