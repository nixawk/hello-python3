#!/usr/bin/python
# -*- coding: utf-8 -*-

# Shallow and Deep Copying

# foo = bar makes the name foo an alias for the object identified as bar.
# In this section, we consider the task of making a copy of an object, rather
# than an alias. This is necessary in applications when we want to
# subsequently modify either the original or the copy in an independent manner.

# shallow copy

    # palette = list(warmtones)
    # In this case, we explicitly call the list constructor, sending the first
    # list as a parameter. This causes a new list to be created, however, it is
    # what is known as a shallow copy. The new list is initialized so that
    # contents are precisely the same as the original sequence. However,
    # Python's lists are referential, and also the new list represents a
    # sequence of references to the same elements as in the first.

# deep copy

    # This is better situation than our first attempt, as we can legitimately
    # add or remove elements from palette without affecting warmnotes.
    # We prefer that palette be what is known as a deep copy of warmtones.
    # In a deep copy, the new copy references its own copies of those
    # references by the original version


import copy


a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]

d = c

print(id(c) == id(d))        # True - d is the same object as c
print(id(c[0]) == id(d[0]))  # True - d[0] is the same object as c[0]

e = copy.copy(c)

print(id(c) == id(e))        # False - e is now a new object
print(id(c[0]) == id(e[0]))  # True - e[0] is the same object as c[0]

f = copy.deepcopy(c)

print(id(c) == id(f))        # False - f is now a new object
print(id(c[0]) == id(f[0]))  # False - f[0] is now a new object


# https://docs.python.org/3/library/copy.html
# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/
# https://stackoverflow.com/questions/17246693/what-exactly-is-the-difference-between-shallow-copy-deepcopy-and-normal-assignm/17246744
