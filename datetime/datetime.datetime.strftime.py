#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
datetime.strftime(format)
    Return a string representing the date and time, controlled by
    an explicit format string. For a complete list of formatting
    directives, see strftime() and strptime() Behavior.

datetime.__format__(format)
    Same as datetime.strftime(). This makes it possible to specify
    a format string for a datetime object in formatted string literals
    and when using str.format(). For a complete list of formatting
    directives, see strftime() and strptime() Behavior.
"""

import datetime


def datetime_datetime_strftime():
    now = datetime.datetime.now()
    print(now.strftime("%Y/%m/%d"))   # 2018/09/09
    print(now.__format__("%Y/%m/%d")) # 2018/09/09


if __name__ == '__main__':
    datetime_datetime_strftime()

# reference
# https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime