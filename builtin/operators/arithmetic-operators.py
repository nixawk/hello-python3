#!/usr/bin/python
# -*- coding: utf-8 -*-

# Arithmetic Operators

# Python supports the following arithmetic operators:

    # +      addition
    # -      substraction
    # *      multiplication
    # /      true division
    # //     integer division
    # %      the modulo operator

# The use of addition, substraction, and multiplication is straightforward,
# nothing that if both operands have type int, then the result is an int as
# well; if one or both operands have type float, the result will be a float.

INT_A = 120
INT_B = 30

print(type(INT_A / INT_B))    # <class 'float'>
print(type(INT_A // INT_B))   # <class 'int'>


FLOAT_A = 120.0
FLOAT_B = 30.0

print(type(FLOAT_A / FLOAT_B))   # <class 'float'>
print(type(FLOAT_A // FLOAT_B))  # <class 'float'>
