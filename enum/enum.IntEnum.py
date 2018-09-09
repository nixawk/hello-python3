#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
class enum.IntFlag
    Base class for creating enumerated constants that can be combined using
    the bitwise operators without losing their IntFlag membership.
    IntFlag members are also subclasses of int.

enum.Enum is immutable.
"""

import enum


@enum.unique
class Person(enum.IntEnum):
    UID = 1
    PID = 0


def enum_IntEnum():
    print(Person.UID.value)
    print(Person.PID.value)


if __name__ == '__main__':
    enum_IntEnum()

# reference
# https://docs.python.org/3/library/enum.html#enum.IntEnum
# https://stackoverflow.com/questions/28126314/adding-members-to-python-enums
