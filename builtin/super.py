#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class PARENT(object):

    def hello(self):
        print("PARENT.hello")

    def __call__(self):
        print("PARENT.__call__")


class CHILD(PARENT):

    def __init__(self, *args, **kwargs):
        super()

    def hello(self):
        print("CHILD.hello")
        super().hello()  # call PARENT.hello()


if __name__ == '__main__':
    child = CHILD()
    child.hello()
    child()


"""
$ py3 super.py
CHILD.hello
PARENT.hello
PARENT.__call__
"""

# references
# https://www.python.org/dev/peps/pep-3135/
