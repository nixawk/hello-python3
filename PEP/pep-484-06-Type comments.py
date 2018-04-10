#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List

# Type comments

# No first-class syntax support for explicitly marking variables as being
# of a specific type is added by this PEP. To help with type inference
# in complex cases, a comment of the following format may be used.

IntArray = []  # type: List[int]
StrArray = []  # type: List[str] 

IntArray[0] = 1234
IntArray[0] = "aaa"  # type: ignore # type error

StrArray[0] = "aaa"
StrArray[0] = 1234   # type error

# Type comments should be put on the last line of the statement that contains
# the variable definition. They can also be placed on with statements and for
# statements, right after the colon.

# A [# type: ignore] comment on a line by itself is equivalent to adding an
# inline [# type: ignore] to each line until the end of the current indented
# block. At top indentation level this effect of disabling type checking until
# the end of file.

    # type: ignore # <comment or other marker>

'''
$ mypy pep-484-06-Type comments.py
pep-484-06-Type comments.py:16: error: No overload variant of "__setitem__" of "list" matches argument types [builtins.int, builtins.str]
pep-484-06-Type comments.py:19: error: No overload variant of "__setitem__" of "list" matches argument types [builtins.int, builtins.int]
'''

# https://www.python.org/dev/peps/pep-0484/#type-comments
# https://www.python.org/dev/peps/pep-0526