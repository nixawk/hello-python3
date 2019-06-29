#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextlib import closing


class MYCLASS(object):

    def __init__(self, *args, **kwargs):
        print("MYCLASS.__init__")

    def __del__(self, *args, **kwargs):
        print("MYCLASS.__del__")

    def __enter__(self):
        print("MYCLSS.__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("MYCLASS.__exit__")

    def hello(self):
        print("MYCLASS.hello")

    def close(self):
        print("MYCLASS.close")


if __name__ == '__main__':
    print("[*] without closing")
    with MYCLASS() as mycls:
        mycls.hello()

    print()
    print("[*] with closing")
    with closing(MYCLASS()) as mycls:
        mycls.hello()

"""
$ [*] without closing
MYCLASS.__init__
MYCLSS.__enter__
MYCLASS.hello
MYCLASS.__exit__

[*] with closing
MYCLASS.__init__
MYCLASS.__del__
MYCLASS.hello
MYCLASS.close
MYCLASS.__del__
"""

# references
# https://www.python.org/dev/peps/pep-0346/
# https://www.python.org/dev/peps/pep-0377/
