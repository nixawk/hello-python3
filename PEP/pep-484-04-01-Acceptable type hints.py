#!/usr/bin/python
# -*- coding: utf-8 -*-

# Acceptable type hints

# Type hints may be built-in classes (including those defined in standard
# library or third-party extension modules), abstract base classes, types
# available in the types module, and user-defined classes (including those
# defined in the standard library or third-party modules).

# While annotations are normally the best format for type hints, there are
# times when it is more appropriate to represent them by a special comment,
# or in a separately distributed stub file.

# Annotations must be valid expressions that evaluate without raising
# exceptions at the time the function is defined (but see below for
# forward references).

from typing import get_type_hints


def annotations_must_be_a_valid_expressions(name: str = "default") -> None:
    print(name)


# Annotations should be kept simple or static analysis tools may not be
# able to interpret the values. For example, dynamically computed types
# are unlikely to be understood.

# In addition to the above, the following special constructs defined
# below may be used: None, Any, Union, Tuple, Callable,
# all ABCs and stand-ins for concrete classes exported from typing
# (e.g. Sequence and Dict), type variables, and type aliases

# All newly introduced names used to support features described in
# following sections (such as Any and Union) are available in the
# typing module.


if __name__ == '__main__':
    annotations_must_be_a_valid_expressions()
    print(get_type_hints(annotations_must_be_a_valid_expressions))


'''
$ py3 pep-484-04-01-Acceptable\ type\ hints.py
default
{'name': <class 'str'>, 'return': <class 'NoneType'>}
'''

## References
# https://www.python.org/dev/peps/pep-0484/#acceptable-type-hints