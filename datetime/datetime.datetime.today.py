#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
classmethod datetime.today()
    Return the current local datetime, with tzinfo None. This is equivalent
    to datetime.fromtimestamp(time.time()). See also now(), fromtimestamp().
"""

import datetime


def datetime_datetime_today():
    print(str(datetime.datetime.today()))   # 2018-09-09 18:40:42.225040


if __name__ == '__main__':
    datetime_datetime_today()


# reference
# https://docs.python.org/3/library/datetime.html#datetime.datetime.today