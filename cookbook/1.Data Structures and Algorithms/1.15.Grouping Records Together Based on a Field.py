#!/usr/bin/python
# -*- coding: utf-8 -*-

# Problem

# You have a sequence of dictionaries or instances and you want to
# iterate over the data in groups based on the value of a particular
# field, such as date.

# Solution

# The itertools.groupby() function is particularly useful for grouping
# data together like this.

from operator import itemgetter
from itertools import groupby
from collections import defaultdict


rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# Sort by the desired field first 
rows.sort(key=itemgetter('date'))

# Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('.   ', i)

# Discussion

# The groupby() function works by scanning a sequence and finding sequential
# 'runs' of identical values (or values returned by the given key function).
# On each iteration, it returns the value along with an iterator that produces
# all of the items in a group with the same value.

# If your goal is to simply group the data together by dates into a large
# data structure that allows random access you may have better luck using
# defaultdict() to build a multidict,

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
print(rows_by_date)
