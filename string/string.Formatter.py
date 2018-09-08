#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
class string.Formatter
"""

import string


class NamespaceFormatter(string.Formatter):
   def __init__(self, namespace={}):
       super(NamespaceFormatter, self).__init__()
       self.namespace = namespace

   def get_value(self, key, args, kwds):
       if isinstance(key, str):
           try:
               # Check explicitly passed arguments first
               return kwds[key]
           except KeyError:
               return self.namespace[key]
       else:
           Formatter.get_value(key, args, kwds)


if __name__ == '__main__':
    fmt = NamespaceFormatter(globals())

    greeting = "hello"
    print(fmt.format("{greeting}, world!"))


# reference
# https://docs.python.org/3.7/library/string.html#custom-string-formatting
# https://www.python.org/dev/peps/pep-3101/
# https://github.com/python/cpython/blob/master/Lib/string.py#L175
