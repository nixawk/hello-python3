#!/usr/bin/python
# -*- coding: utf-8 -*-

from ctypes import *


"""
class ctypes.Structure(*args, **kw)

    Abstract base class for structures in native byte order.

    Concrete structure and union types must be created by subclassing one of
    these types, and at least define a _fields_ class variable. ctypes will
    create descriptors which allow reading and writing the fields by direct
    attribute accesses. These are the

    _fields_

        A sequence defining the structure fields. The items must be 2-tuples or
        3-tuples.

         - The first item is the name of the field,
         - The second item specifies the type of the field; it can be any ctypes data type.
         - The third optional item can be given. It must be a small positive integer defining
           the bit width of the field.

         Field names must be unique within one structure or union. This is not
         checked, only one field can be accessed when names are repeated.

         It is possible to define the _fields_ class variable after the class
         statement that defines the Structure subclass, this allows creating
         data types that directly or indirectly reference themselves

            class List(Structure):
                pass

            List._fields_ = [
                ("id", c_ubyte)
            ]

         The _fields_ class variable must, however, be defined before the type
         is first used (an instance is created, sizeof() is called on it, and
         so on). Later assignment to the __fields_ class variable will raise
         an AttributeError.

         It is possible to defined sub-class of structure types, they inherit
         the fields of the base class plus the _fields_ defined in the sub-subclass,
         if any.


"""

class StructObj(Structure):
    def __init__(self):
        pass


if __name__ == '__main__':
    StructObj._fields_ = [
        ('id', c_ubyte),
        ('age', c_ulong)
    ]

    so = StructObj()
    print(so.id)
    print(so.age)
