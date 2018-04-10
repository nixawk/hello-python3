#!/usr/bin/python
# -*- coding: utf-8 -*-

# Imports should usually be on separate lines,

import os
import sys  # No: import os, sys

from subprocess import Popen, PIPE

# Imports are always put at the top of the file, just after any module
# comments and docstrings, and before module globals and constants.

# Imports should be grouped in the following order
# 1. standard library imports
# 2. related third party imports
# 3. local application/library specific imports

# You should put a blank line between each group of imports.

# Absolute imports are recommeded, as they are usually more readable and
# tend to be better behaved (or at least give better error messages) if
# the import system is incorrectly configured.

# However, explicit relative imports are an acceptable alternative to
# absolute imports, especially when dealing with complex package layouts
# where using absolute imports would be unnecessarily verbose.

# Standard library code should avoid complex package layouts and always
# use absolute imports.

# When importing a class from a class-containing module, it's usually
# okay to spell this

# from myclass import MyClass
# from foo.bar.yourclass import YourClass

# Wildcard imports (from <module> import *) should be avoided, as they
# make it unclear which names are present in the namespace, confusing
# both readers and many automated tools. There is one defensible use
# case for a wildcard import, which is to republish an internal interface
# as part of a public API (for example, overwriting a pure Python
# implementation of an interface with the definitions from an
# optional accelerator module and exactly which definitions will
# be overwritten isn't known in advance).

# https://www.python.org/dev/peps/pep-0008/#imports
