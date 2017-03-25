#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
The Null Object

This object is returned  by functions that don't explicitly return a value.
It supports no special operations. There is exactly one null object, named None
(a built-in name). type(None)() produces the same singleton.
"""

print(None.__class__())
print(None.__bool__())
