#!/usr/bin/python
# -*- coding: utf-8 -*-

# The meaning of annotations

# Any function without annotations should be treated as having general type
# possible, or ignored, by any type checker. Functions with the @no_type_check
# decorator should be treated as having no annotations.

# It is recommended but not required that checked functions have annotations
# for all arguments and the return type. For a checked function, the default
# annotation for arguments and for the return type is Any. An exception is the
# first argument of instance and class methods. If it is not annotated, then
# it is assumed to have the type of the containing class for instance methods,
# and a type object type corresponding to the containing class object for class
# methods. For example, in class A the first argument of an instance method has
# the implicit type A. In a class method, the precise type of the first argument
# cannot be represented using the available type notation.


from typing import (
    no_type_check,
    get_type_hints
)


@no_type_check
def test1(name: str) -> None:
    pass


def test2(name: str) -> None:
    pass


if __name__ == '__main__':
    print(get_type_hints(test1))
    print(get_type_hints(test2))


'''
$ python3 pep-484-03-The\ meaning\ of\ annotations.py
{}
{'name': <class 'str'>, 'return': <class 'NoneType'>}
'''

## References
# https://www.python.org/dev/peps/pep-0484/#the-meaning-of-annotations