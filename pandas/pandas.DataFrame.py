#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas


"""
In [25]: pandas.DataFrame([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], columns=['AAAAAAAA', 'BBBBBBB'], index=dates)
Out[25]:
            AAAAAAAA  BBBBBBB
2017-06-01         1        1
2017-06-02         2        2
2017-06-03         3        3
2017-06-04         4        4
2017-06-05         5        5
2017-06-06         6        6
"""


dates = pandas.date_range('20170601', periods=6)
datas = pandas.DataFrame(
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6)
    ],
    columns=['AAAAAAAA', 'BBBBBBB'],
    index=dates)


print(datas)


## References

# http://pandas.pydata.org/pandas-docs/stable/10min.html