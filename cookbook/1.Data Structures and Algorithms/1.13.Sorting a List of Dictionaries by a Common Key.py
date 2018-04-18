#!/usr/bin/python
# -*- coding: utf-8 -*-

# Problem

# You have a list of dictionaries and you would like to sort the entries
# according to one or more of the dictionary values.

# Solution

# Sorting this type of structure is easy using the operator module's
# itemgetter function. Let's say you've queried a data table to get
# a listing of the members on your website, and you receive the following
# data structure in return.

# The operator.itemgetter() function takes as arguments the lookup indices
# used to extract the desired values from the records in rows. It can be
# a dictionary key name, a numeric list element, or any value that can be
# fed to an object's __getitem__() method. If you give multiple indices to
# itemgetter(), the callable it produces will return a tuple with all of
# the elements in it, and sorted() will order the output according to the
# sorted order of the tuples.

# The functionality of itemgetter() is sometimes replaced by lambda expressions.


from operator import itemgetter


class Item:

    def __init__(self, value):
        self.value = value

    def __getitem__():
        return self.value


rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# The itemgetter() function can also accept multiple keys.

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))

print(rows_by_fname)
print(rows_by_uid)

print(itemgetter(Item('hello world')))



