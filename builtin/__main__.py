#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Many Python modules are also intended to be called as standalone scripts.

# The standard name of the 'main function' should be __main__.
# When a module is invoked on the command line, such as:

    # python mymodule.py

# then the module behaves as though the following lines existed at the end of
# the module (except that the attribute __sys may not be used or assumed to
# exist elsewhere in the script):

    # if globals().has_key("__main__"):
    #     import sys as __sys
    #     __sys.exit(__main__(__sys.argv))


# Should the return value from __main__ be treated as the exit value ?

    # Yes. Many __main__ will naturally return None, which sys.exit translates
    # into a "succes" return code. In those that return a numeric result, it
    # behaves just like the argument to sys.exit() or the return value from C's
    # main().

import sys


if __name__ == '__main__':
    print(hasattr(globals(), "__main__"))
    sys.exit(0)


# references
# https://www.python.org/dev/peps/pep-0299/
