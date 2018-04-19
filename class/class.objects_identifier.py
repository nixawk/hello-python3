#!/usr/bin/python
# -*- coding: utf-8 -*-

# Objects in Python

# Python is an object-oriented language and classes from the basic for all
# data types. In this section, we describe key aspects of Python's object
# model, and we introduce Python's built-in classes, such as the int class
# for integers, the float class for floating-point values, and the str
# class for character strings.

# Identifiers

# Identifiers in Python are case-sensitive, so temperature and Temperature
# are distinct names. Identifiers can be composed of almost any combination
# of letters, numerals, and underscore characters. Each identifier is
# implicitly associated with the memory address of the object to which it
# refers. A Python identifier may be assigned to a soecial object named
# None, serving a similar purpose to a null reference in Java or C++.

# Unlike Java and C++, Python is a dynamically typed language, as there is
# no advance declaration associating an identifier with a particular data
# type. An identifier can be associated with any type of object, and it
# can later be reassigned to another object of the same (or different) type.

# Reserved Words

# False None True and as assert break class continue def del elif
# else except finally for from global if import in is lambda
# nonlocal not or pass raise return try while with yield

temperature = 98.6

print(id(temperature))

temperature = temperature + 5.0

print(id(temperature))

# The execution of this command begins with the evaluation of the expression
# on the right-hand side of the = operator. That expression, temperature + 5.0,
# is evaluated based on the existing binding of the name temperature, and so
# the result has value 103.6. That result is stored as a new floating-point
# instance, and only then is the name on the left-hand side of the assignment
# statement, temperature, (re)assigned to the result.
