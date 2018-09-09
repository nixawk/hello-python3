#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
class datetime.datetime
    A combination of a date and a time. Attributes: year, month,
    day, hour, minute, second, microsecond, and tzinfo.
"""

import datetime


def datetime_datetime():
    # def __new__(cls, year, month=None, day=None, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0):
    _datetime = datetime.datetime(
        2018,
        month=8,
        day=8,
        hour=8,
        minute=0,
        second=0
    )
    print(str(_datetime))  # 2018-08-08 08:00:00


if __name__ == '__main__':
    datetime_datetime()


# reference
# https://docs.python.org/3/library/datetime.html
