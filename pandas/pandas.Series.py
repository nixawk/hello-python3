#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)


"""
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64
"""

## Referencea
# http://pandas.pydata.org/pandas-docs/stable/10min.html