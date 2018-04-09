#!/usr/bin/python
# -*- coding: utf-8 -*-

# User-defined generic types

# You can include a Generic base class to define a user-defined class
# as generic.

from typing import (
    TypeVar,
    Generic
)


# A generic type can have any number of type variables, and type
# variables may be constrained. Each type variable argument to
# Generic must be distinct.

T = TypeVar('T')
S = TypeVar('S')


class Generic_Types(Generic[T, S]):

    def greeting(self, msg: str) -> None:
        print("Hello " + msg)


if __name__ == '__main__':
    gt = Generic_Types()
    gt.greeting('Python')


# https://www.python.org/dev/peps/pep-0484/#user-defined-generic-types