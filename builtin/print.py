#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
When the right argument is a dictionary (or other mapping type),
then the formats in the string must include a parenthesised mapping key into
that dictionary inserted immediately after the '%' character. The mapping key
selects the value to be formatted from the mapping.

d - Signed integer decimal.
i - Signed integer decimal.
o - Signed octal value.
u - Obsolete type - it is idential to 'd'
x - Signed hexadecimal (lowercase)
X - Signed hexadecimal (uppercase)
e - floating point exponential format (lowercase)
E - floating point exponential format (uppercase)
f - floating point decimal format
F - floating point decimal format
g - Floating point format
G - Floating point format
c - Single character (accepts integer or single character string)
r - String (converts any Python object using repr())
s - String (converts any Python object using str())
a - String (converts any Python object ascii())
% - No argument is converted, results in a '%' character in the result.
"""

print("%(language)s has %(number)03d quote types." % {
    'language': "Python",
    'number': 2
})


# references
# https://docs.python.org/3.7/library/stdtypes.html#printf-style-string-formatting
