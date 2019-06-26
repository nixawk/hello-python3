#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextvars import ContextVar


def main():
    var: ContextVar[int] = ContextVar('var', default=42)

    # The name of the variable. This is a read-only property.
    print(var.name)
    
    print(var.get())
    token = var.set(100)
    print(var.get())

    var.reset(token)
    print(var.get())


if __name__ == '__main__':
    main()

"""
$ py3 contextvars.ContextVar.py
var
42
100
42
"""

# references
# https://docs.python.org/3/library/contextvars.html#module-contextvars
