#!/usr/bin/python
# -*- coding: utf-8 -*-

from itertools import compress

# Problem

# You have data inside of a sequence, and need to exract values or reduce
# the sequence using some criteria.

# Solution

# The easiest way to filter sequence data is often to use a list comprehension.

    # >>> mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    # >>> [n for n in mylist if n > 0]
    # [1, 4, 10, 2, 3]
    # >>> [n for n in mylist if n < 0]
    # [-5, -7, -1]
    # >>>

# One potential downside of using a list comprehension is that it might produce
# a large result if the original input is large. If this is a concern, you can
# use generator expressions to produce the filtered values iteratively.

    # >>> pos = (n for n in mylist if n > 0)
    # >>> pos
    # <generator object <genexpr> at 0x1006a0eb0>
    # >>> for x in pos:
    # ... print(x)
    # ...

# Sometimes, the filtering criteria cannot be easily expressed in a list
# comprehension or generator expression. For example, suppose that the
# filtering process involves exception handling or some other complicated
# detail. For this, put the filtering code into its own function and use
# the builtin-in filter() function.

# filter() creates an iterator, so if you want to create a list of results,
# make sure you also use list() as shown.

mylist = [1, 4, -5, 10, -7, 2, 3, -1]

print(list(filter(lambda x: x > 0, mylist)))

# Discussion

# List comprehensions and generator expressions are often the easiest and
# most straight forward ways to filter simple data. They also have the added
# power to transform the data at the same time.

# Another notable filtering tool is itertools.compress(), which takes an
# iterable and an accompanying Boolean selector sequence as input.

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W CRANVILLE'
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

more5 = [c > 5 for c in counts]

print(list(compress(addresses, more5)))

# The key here is to first create a sequence of Booleans that indicates which
# elements satisfy the desired condition. The compress() function then picks
# out the items corresponding to True values.

# Like filter(), compress() normally returns an iterator. Thus, you need to use
# list() to turn the results into a list if desired.
