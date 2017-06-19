#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
def date_range(start=None, end=None, periods=None, freq='D', tz=None,
               normalize=False, name=None, closed=None, **kwargs):
    
    Return a fixed frequency datetime index, with day (calendar) as the default
    frequency

    Parameters
    ----------
    start : string or datetime-like, default None
        Left bound for generating dates
    end : string or datetime-like, default None
        Right bound for generating dates
    periods : integer or None, default None
        If None, must specify start and end
    freq : string or DateOffset, default 'D' (calendar daily)
        Frequency strings can have multiples, e.g. '5H'
    tz : string or None
        Time zone name for returning localized DatetimeIndex, for example
        Asia/Hong_Kong
    normalize : bool, default False
        Normalize start/end dates to midnight before generating date range
    name : str, default None
        Name of the resulting index
    closed : string or None, default None
        Make the interval closed with respect to the given frequency to
        the 'left', 'right', or both sides (None)
"""

import pandas
import numpy


dates = pandas.date_range('2017-01-01', periods=6)
print(dates)

# dates = pandas.date_range('2017-01-01', periods=6, freq='12H')
# print(dates)


df = pandas.DataFrame(numpy.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(df)

"""
DatetimeIndex(['2017-01-01', '2017-01-02', '2017-01-03', '2017-01-04',
               '2017-01-05', '2017-01-06'],
              dtype='datetime64[ns]', freq='D')
DatetimeIndex(['2017-01-01 00:00:00', '2017-01-01 12:00:00',
               '2017-01-02 00:00:00', '2017-01-02 12:00:00',
               '2017-01-03 00:00:00', '2017-01-03 12:00:00'],
              dtype='datetime64[ns]', freq='12H')
"""