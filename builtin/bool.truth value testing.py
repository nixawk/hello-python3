#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Truth Value Testing

Any object can be tested for truth value, for use in an if or while condition
or as operand of the Boolean operations below.

By default, an object is considered true unless its class defines either a
__bool__() method that returns False or a __len__() method that  returns zero,
when called with the object. Here are most of the built-in objects considered
false:

    - constants defined to be false: None and False
    - zero of any numberic type: 0, 0.0, 0j, Decimal(0), Fracion(0, 1)
    - empty sequences and collections: '', (), [], set(), range(0)
"""

class MyBoolObject1(object):

    def __bool__(self):
        return True


class MyBoolObject2(object):

    def __len__(self):
        return 0


if __name__ == '__main__':
    if bool(MyBoolObject1()):
        print("It's true")     # output
    else:
        print("It's false")

    if bool(MyBoolObject2()):
        print("It's true")
    else:
        print("It's false")    # output


# references
# https://docs.python.org/3.7/library/stdtypes.html#truth-value-testing
