#!/usr/bin/enc python3
# -*- coding: utf-8 -*-

"""
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
"""

def write_to_file_with_print(filename, data):
    with open(filename, 'a') as fileobject:
        print(data, file=fileobject, flush=True)


if __name__ == '__main__':
    write_to_file_with_print('/tmp/testfile', 'This is a demo string by print.')
    write_to_file_with_print('/tmp/testfile', u'Hello россия')
