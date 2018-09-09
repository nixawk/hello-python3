#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
classmethod datetime.now(tz=None)
    Return the current local date and time. If optional argument tz
    is None or not specified, this is like today(), but, if possible,
    supplies more precision than can be gotten from going through
    a time.time() timestamp (for example, this may be possible on
    platforms supplying the C gettimeofday() function).

    If tz is not None, it must be an instance of a tzinfo subclass,
    and the current date and time are converted to tz’s time zone.
    In this case the result is equivalent to
    tz.fromutc(datetime.utcnow().replace(tzinfo=tz)).
    See also today(), utcnow().
"""

import datetime


def datetime_datetime_now():
    print(str(datetime.datetime.now()))       # 2018-09-09 18:47:30.002969
    print(str(datetime.datetime.utcnow()))    # 2018-09-09 10:47:30.003026


if __name__ == '__main__':
    datetime_datetime_now()

# reference
# https://docs.python.org/3/library/datetime.html#datetime.datetime.now