#!/usr/bin/python
# -*- coding: utf-8 -*-

# Rationale and Goals

# This PEP aims to provide a standard syntax for type annotations,
# opening up Python code to easier static analysis and redactoring,
# potential runtime type checking, and (perhaps, in some contexts)
# code generation utilizing type information.

## Non-goals

# While the proposed typing module will contains some building blocks
# for runtime type checking -- in particular the get_type_hints()
# function -- third party packages would have to be developed to 
# implemented specific runtime type checking functionality,
# for example using decorators or metaclasses. Using type hints
# for performance optimization is left as an exercise for the
# reader.

# It should also be emphasized that Python will remain a dynamically
# typed language, and the authors have no desire to ever make type
# hints mandatory, even by convention.

from typing import Dict
from typing import get_type_hints


def _get_type_hints(module_class_method_function) -> dict:
    # TypeError: 'typing_hints' is not a module, class, method, or function.
    return get_type_hints(module_class_method_function)


def greeting(name: str) -> None:
    return "Hello " + name


if __name__ == '__main__':
    hints = _get_type_hints(greeting)
    print(hints)


'''
$ python pep-484-02-Rational\ and\ Goals.py
{'name': <class 'str'>, 'return': <class 'NoneType'>}
'''

## References

# https://www.python.org/dev/peps/pep-0484/
# https://www.python.org/dev/peps/pep-0484/#non-goals