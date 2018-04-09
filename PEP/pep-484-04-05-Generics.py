#!/usr/bin/python
# -*- coding: utf-8 -*-

# Generics

# Since type information about objects kept in containers cannot
# be statically inferred in a generic way, abstract base classes
# have been extended to support subscription to denote expected
# types for container elements.

# Generics can be parameterized by using a new factory available
# in typing called TypeVar.

# A TypeVar() expression must always directly be assigned to a
# variable. The argument to TypeVar() must be a string equal to
# the variable name to which it is assigned. Type variables must
# not be redefined.


from typing import (
    TypeVar,
    Sequence
)


T = TypeVar('T')


def print_sequence(seq: Sequence[T]) -> None:
    for _ in seq:
        print(_)


if __name__ == '__main__':
    print_sequence([1, 2, 3, 4, 5])


# https://www.python.org/dev/peps/pep-0484/#generics