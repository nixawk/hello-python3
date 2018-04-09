#!/usr/bin/python
# -*- coding: utf-8 -*-

# Type Definition Syntax

# The syntax leverages PEP 3107-style annotations with a number of
# extensions described in sections below. In its basic form,
# type hinting is used bt filling function annotation slots with
# classes:

def greeting(name: str) -> str:
    return "Hello " + name


# This states that the expected type of the name argument is str.
# Analogically, the expected return type str is str.

# Expressions whose type is a subtype of a specfic argument type
# are also accepted for that argument.


if __name__ == '__main__':
    print(greeting('Python'))


# https://www.python.org/dev/peps/pep-3107
# https://www.python.org/dev/peps/pep-0484/#type-definition-syntax