#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
importlib.__import__(name, globals=None, locals=None, fromlist=(), level=0)
An implementation of the built-in __import__() function.

importlib.import_module(name, package=None)
Import a module. The name argument specifies what module to import in
absolute or relative terms (e.g. either pkg.mod or ..mod). If the name
is specified in relative terms, then the package argument must be set
to the name of the package which is to act as the anchor for resolving
the package name
(e.g. import_module('..mod', 'pkg.subpkg') will import pkg.mod).

The import_module() function acts as a simplifying wrapper around
importlib.__import__(). This means all semantics of the function
are derived from importlib.__import__().

The most important difference between these two functions is that
import_module() returns the specified package or module (e.g. pkg.mod),
while __import__() returns the top-level package or module (e.g. pkg).
"""

import importlib


def importlib_import_module():
    mod = importlib.import_module('mod')
    mod.greeting()


if __name__ == '__main__':
    importlib_import_module()


# reference
# https://docs.python.org/3/library/importlib.html