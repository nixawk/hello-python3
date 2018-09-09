#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
class datetime.timedelta
    A duration expressing the difference between two date, time,
    or datetime instances to microsecond resolution.
"""

import datetime


def datetime_timedelta():
    # def __new__(cls, days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0):
    _timedelta = datetime.timedelta(
        days=1,
        seconds=0,
        microseconds=0,
        milliseconds=0,
        minutes=0,
        hours=0,
        weeks=1
    )
    print(str(_timedelta))    # 8 days, 0:00:00


if __name__ == '__main__':
    datetime_timedelta()

# reference
# https://docs.python.org/3/library/datetime.html
