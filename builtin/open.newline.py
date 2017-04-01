#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
'U'       universal newline mode (deprecated)
"""

with open('/etc/passwd', 'r', newline='\r\n') as f:
    for _ in f:
        print(repr(_))

# newline controls how universal newlines works (it only applies to text
# mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
# follows:
