#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
classmethod datetime.strptime(date_string, format)
    Return a datetime corresponding to date_string, parsed according
    to format. This is equivalent to
    datetime(*(time.strptime(date_string, format)[0:6])).
    ValueError is raised if the date_string and format can’t be parsed
    by time.strptime() or if it returns a value which isn’t a time tuple.
    For a complete list of formatting directives,
    see strftime() and strptime() Behavior.
"""

import datetime


def datetime_datetime_strptime():
    _datetime = datetime.datetime.strptime(
        "2018-09-09 18:47:30",
        "%Y-%m-%d %H:%M:%S"
    )
    print(str(_datetime))


if __name__ == '__main__':
    datetime_datetime_strptime()

# reference
# https://docs.python.org/3/library/datetime.html#datetime.datetime.strptime
# https://docs.python.org/3/library/time.html#time.strftime
