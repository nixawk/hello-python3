#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
class datetime.time
    An idealized time, independent of any particular day, assuming that every
    day has exactly 24*60*60 seconds (there is no notion of “leap seconds”
    here). Attributes: hour, minute, second, microsecond, and tzinfo.
"""

import datetime


def datetime_time():
    # def __new__(cls, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0):
    time = datetime.time(hour=8, minute=30, second=0, microsecond=0)
    print(str(time))     # 08:30:00


if __name__ == '__main__':
    datetime_time()


# reference
# https://docs.python.org/3/library/datetime.html
