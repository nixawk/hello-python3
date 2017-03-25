#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Instance of a class cannot be ordered with respect to other instances of
the same class, or other types of object, unless the class defines enough
of the methods

    __lt__()
    __le__()
    __gt__()
    __ge__()

The behavior of the is and is not operators cannot be customized; also they
can be applied to any two objects and never raise an exception.

"""


class Comparisons(object):
    def __eq__(self, obj):
        return isinstance(obj, self.__class__)


c1 = Comparisons()
c2 = Comparisons()

print(c1 == c2)
