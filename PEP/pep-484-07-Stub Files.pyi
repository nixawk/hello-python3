#!/usr/bin/python
# -*- coding: utf-8 -*-

# Notice: This is a Stub file


# Stub Files

## Function/method overloading

# The @overload decorator allows describing functions and methods that
# support multiple different combinations of argument types. This
# pattern is used frequently in builtin modules and types.

from typing import overload


class MyClass:

    @overload
    def foo(self, name: str) -> None: ...

    @overload
    def foo(self, num: int) -> None: ...

# Uses of the @overload decorators as shown above are suitable for
# stub files. In regular modules, a series of @overload-decorated
# definitions must be followed by exactly one non-@overload-decorated
# definition (for the same function/method). The @overload-decorated
# definitions are for the benefit of the type checker only, since
# they will be overwritten by the non-@overload-decorated definition,
# while the latter is usead at runtime but should be ignored by a
# type checker. At runtime, calling a @overload-decorated function
# will raise NotImplementedError. Here's an example of a non-stub
# overload that can't easily be expressed using a union or a type
# variable.

'''
NotImplementedError: You should not call an overloaded function.
A series of @overload-decorated functions outside a stub module
should always be followed by an implementation that is not @overload-ed.
'''

'''
$ stubgen -h
usage: stubgen [--py2] [--no-import] [--doc-dir PATH]
               [--search-path PATH] [-p PATH] [-o PATH]
               MODULE ...

Generate draft stubs for modules.

Stubs are generated in directory ./out, to avoid overriding files with
manual changes.  This directory is assumed to exist.

Options:
  --py2           run in Python 2 mode (default: Python 3 mode)
  --recursive     traverse listed modules to generate inner package modules as well
  --ignore-errors ignore errors when trying to generate stubs for modules
  --no-import     don't import the modules, just parse and analyze them
                  (doesn't work with C extension modules and doesn't
                  respect __all__)
  --include-private
                  generate stubs for objects and members considered private
                  (single leading undescore and no trailing underscores)
  --doc-dir PATH  use .rst documentation in PATH (this may result in
                  better stubs in some cases; consider setting this to
                  DIR/Python-X.Y.Z/Doc/library)
  --search-path PATH
                  specify module search directories, separated by ':'
                  (currently only used if --no-import is given)
  -p PATH         use Python interpreter at PATH (only works for
                  Python 2 right now)
  -o PATH         Change the output folder [default: out]
  -h, --help      print this help message and exit
'''

# https://www.python.org/dev/peps/pep-0484/#function-method-overloading
# https://github.com/python/typing/issues/72
# https://stackoverflow.com/questions/35602541/create-pyi-files-automatically/35706456#35706456