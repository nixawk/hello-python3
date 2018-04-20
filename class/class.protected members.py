#!/usr/bin/python
# -*- coding: utf-8 -*-

# Protected Members

# The underscored name, by convention, suggests that this is a nonpublic member,
# so we might ask if it is okay that we access it in this fashion. While
# general users of the class should not be doing so, our subclass has a
# somewhat privileged relationship with the superclass.

# Python does not support formal access control, but names beginning with
# a single underscore are conventionally akin to protected, while names
# beginning with a double underscore (other than special methods) are akin
# to private.

__all__ = ['MyClass']


class MyClass:

    def _protected_method(self):
        print("protected method")

    def __private_method(self):
        print("private method")

    def public_method(self):
        print("public method")


if __name__ == '__main__':
    mycls = MyClass()
    print(dir(mycls))
