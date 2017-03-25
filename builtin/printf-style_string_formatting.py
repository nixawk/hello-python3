#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
When the right argument is a dictionary (or other mapping type),
then the formats in the string must include a parenthesised mapping key into
that dictionary inserted immediately after the '%' character. The mapping key
selects the value to be formatted from the mapping.
"""

print("%(language)s has %(number)03d quote types." % {
    'language': "Python",
    'number': 2
})
