#!/usr/bin/python
# -*- coding: utf-8 -*-

# Code in the core Python distribution should always use UTF-8
# (or ASCII in Python 2).

# Files using ASCII (in Python 2) or UTF-8 (in Python 3) should
# not have an encoding declaration.

# In the standard library, non-default encodings should be used
# only for test purposes or when a comment or docstring needs to
# mention an author name that contains non-ASCII characters;
# otherwise, using \x, \u, \U, or \N escapes is the preferred
# way to include non-ASCII data in string literals.

# For Python 3.0 and beyond, the following policy is prescribed
# for the standard library (see PEP 3131): All identifiers in the
# Python standard library MUST use ASCII-only identifiers, and
# SHOULD use English words wherever feasible (in many cases,
# abbreviations and technical terms are used which aren't English).
# In addition, string literals and comments must also be in ASCII.
# The only exceptions are (a) test cases testing the non-ASCII features,
# and (b) names of authors. Authors whose names are not based on
# the Latin alphabet (latin-1, ISO/IEC 8859-1 character set) MUST
# provide a transliteration of their names in this character set.

print(u'\u4e16\u754c')

# https://www.python.org/dev/peps/pep-0008/#source-file-encoding
