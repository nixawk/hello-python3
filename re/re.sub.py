#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
re.sub(pattern, repl, string, count=0, flags-0)

    Return the string obtained by replacing the leftmost non-overlapping
    occurrences of pattern in string by the replacement repl.
    If the pattern isn't found, string is returned unchanged.
    repl can be a string or a function; if it is a string, any backslash escapes
    in it are processed. That is, \n is converted to a single newline character,
    \r is converted to a carriage return, and so forth. Unknown escapes such as
    \& are left alone. Backreferences, such as \6, are replaced with the
    substring matched by group 6 in the pattern.

re.subn(pattern, repl, string, count=0, flags=0)

    Perform the same operation as sub(), but return a tuple
    (new_string, number_of_subs_made).
"""

import re


s = "____ is a good choice."
print(re.sub(r'_+', 'Python', s))
print(re.subn(r'_+', 'Python', s))
