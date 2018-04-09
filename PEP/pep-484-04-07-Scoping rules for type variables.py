#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import (
    TypeVar,
    Generic
)

# A type variable used in generic function could be inferred to represent
# different types in the same code block.

T = TypeVar('T')


def func_1(x: T):   # T here
    print(x)


def func_2(x: T):   # T could be different
    print(x)


# A type variable used in a method of generic class that coincides with
# one of the variables that paramererize this class is always bound to
# that variables.

class MyClass(Generic[T]):

    def foo_1(self, x: T) -> T:  # T here
        return x

    def foo_2(self, x: T) -> T:  # and here are always the same
        return x

# A type variable used in a method that does not match any of the variables
# that parameterize the class makes this method a generic function in that
# variable.

# Unbound type variables should not appear in the bodies of generic functions,
# or in the class bodies apart from method definitions.

# A generic class definition that appears inside a generic function should
# not use type variables that parameterize the generic function.

# A generic class nested in another generic class cannot use same type variables.


if __name__ == '__main__':
    func_1(123)     # This is OK, T is inferred to be int. 
    func_2('aaa')   # This is also OK, now T is str.

    a = MyClass()   # type: MyClass[int] 
    a.foo_1(1)      # OK
    # a.foo_2('a')    # This is an error


# https://www.python.org/dev/peps/pep-0484/#scoping-rules-for-type-variables