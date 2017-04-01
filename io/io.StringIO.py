#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Init signature: io.StringIO(initial_value='', newline='\n')
Docstring:
Text I/O implementation using an in-memory buffer.

The initial_value argument sets the value of object.  The newline
argument is like the one of TextIOWrapper's constructor.
"""

import io


s = io.StringIO()
s.write('helloworld\n')
data = s.getvalue()
print(data)

s = io.StringIO(initial_value='helloworld\n')
data = s.getvalue()
print(data)
