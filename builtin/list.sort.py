#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Lists are mutable sequences, typically used to store collections
of homogeneous items (where the precise degree of similarly will
vary by applications).

class list([iterator])

    Lists may be constructed in several ways:

    - Using a pair of square brackets to denote the empty list: []
    - Using square brackets, separating items with commas: [a], [a, b, c]
    - Using a list comprehension: [x for x in iterable]
    - Using the type constructor: list() or list(iterator)

sort(*, key=None, reverse=False)

    This method sorts the list in place, using only < comparisons
    between items. Exceptions are not supported - if any comparison
    operations fail, the entire sort operation will fail (and the
    list will likely be left in a partially modified state)

    key specifies a function of one argument that is used to extract
    a comparison key from each list element (for example, key=str.lower).
    The key corresponding to each item in the list is calculated once
    and then used for the entire sorting process. The default value
    of None means that list items are sorted directly without calculating
    a separate key value.

    The functools.cmp_to_key() utility is available to convert a 2.x style
    cmp function to a key function.

    reverse is a boolean value. If set to True, then the list elements
    are sorted as if the comparison were reversed.

What's the differences between list().sort() and sorted() ?

    This method modifies the sequence in place for economy of space when
    sorting a large sequence. To remind users that it operates by side
    effect, it does not return the sorted sequence (use sorted() to
    explicitly request a new sorted list instance).
"""

languages = [
    "c",
    "c++",
    "python",
    "java",
    "ruby",
    "golang",
    "shell"
]

# a new sorted list is created.
print(sorted(languages, key=len, reverse=False))

# the original list is changed.
languages.sort(key=len, reverse=False)  # sort by length
print(languages)


# references
# https://docs.python.org/3.7/library/stdtypes.html#lists
