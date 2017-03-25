#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
str.encode(encoding="utf-8", errors="strict")

    Return an encoded version of the string as bytes object. Default
    encoding is 'utf-8'. errors may be given to set a different error
    handling scheme. The default for errors is 'strict', meaning that
    encoding errors raise a UnicodeError. Other possible values are
    'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' and
    any other name registered via codecs.register_error().
"""

"""
Traceback (most recent call last):
  File "str.encode.py", line 17, in <module>
    print(s.encode('utf-8'))
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 0: ordinal not in range(128)

# Please try python3
"""

s = 'ß'

print(s.encode('utf-8'))
