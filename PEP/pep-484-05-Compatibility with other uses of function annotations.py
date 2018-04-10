#!/usr/bin/python
# -*- coding: utf-8 -*-

# Compatiability with other uses of function annotations

# A number of existing or potential use cases for function annotations exist,
# which are incompatible with type hinting. These may confuse a static type
# checker. However, since type hinting annotations have no runtime behavior
# (other than evaluation of the annotation expression and storing annotations
# in __annotations__ attribute of the function object), this does not make
# the program incorrect -- it just cause a type checker to emit spurious
# warnings or errors.

# To make portions of the program that should not be covered by type hinting,
# you can use one or more of the following:

    # a # type: ignore comment;
    # a @no_type_check decorator on a class or function;
    # a custom class or function decorator marked with @no_type_check_decorator.

from typing import(
    no_type_check,
    TypeVar,
    Generic
)


@no_type_check
def demo_no_type_check(name: str = "Python") -> None:
    print(name)


def demo_type_ignore_comment(name: str = "Python") -> None:
    print(name)

# In order for maximal compatibility with offline type checking it may eventually
# be a good idea to change interfaces that rely on annotations to switch to a
# different mechanism, for example a decorator.

demo_no_type_check()
demo_type_ignore_comment(123)  # type: ignore

# If not [type: ignore], mypy shows

'''
$ mypy "pep-484-05-Compatibility with other uses of function annotations.py"
pep-484-05-Compatibility with other uses of function annotations.py:41: error: Argument 1 to "demo_type_ignore_comment" has incompatible type "int"; expected "str"
'''

# https://www.python.org/dev/peps/pep-0484/#compatibility-with-other-uses-of-function-annotations