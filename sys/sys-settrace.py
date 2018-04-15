#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def tracefunc(frame, event, arg):
    print(frame.f_lineno, event)
    return tracefunc


def greeting():
    friends = ["Keen", "Linada", "Python"]
    for f in friends:
        print(f)
    return len(friends)


sys.settrace(tracefunc)
greeting()

"""
$ py3 sys-settrace.py
12 call
13 line
14 line
15 line
Keen
14 line
15 line
Linada
14 line
15 line
Python
14 line
16 line
16 return
27 call
27 exception
27 return
"""

## References
# http://pyvideo.org/pycon-us-2017/debugging-in-python-36-better-faster-stronger.html