#!/usr/bin/python
# -*- coding: utf-8 -*-

# Names to Avoid

# Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh),
# or 'I' (uppercase letter eye) as single character variable names.

# ASCII Compatibility

# Identifiers used in the standard library must be ASCII compatible as described
# in the policy section of PEP 3131

# Package and Module Names

# Modules should have short, all-lowercase names. Underscores can be used in the
# module name if it improves readability. Python packages should also have short
# , all-lowercase names. although the use of underscores is discouraged.

# When an extension module written in C or C++ has an accompanying Python module
# that provides a higher level interface, the C/C++ module has a leading
# underscore.

# Class Names

# Class names should normally use the CapWords convention.
# The naming convention for functions may be used instead in cases where the
# interface is documented and used primarily as a. callable.

class MyClassOne(object):

    @classmethod
    def greeting(cls):
        """This is a example for Class Names
        """
        print("This is my class")

# Type variable names

# Names of type variable introduced in PEP 484 should normally use CapWords
# preferring short names: T, AnyStr, Num.

# It is recommended to add suffixes _co or _contra to the variables used to
# declare covariant or contravariant behavior correspondingly.

# Exception Names

# Because exceptions should be classes, the class naming convention applies
# here. However, you should use the suffix "Error" on your exception names
# (if the exception actually is an eror).

# Global Variable Names

# Modules that are designed for use via from M import * should use the
# __all__ mechanism to prevent exporting globals, or use the older convention
# of prefixing such globals with an underscore (which you might want to do
# indicare these globals are "module non-public")

_GLOBALVAR = "Just for Global Variable Names"

# Function and variable names

# Function names should be lowercase, with words separated by underscore as
# necessary to improve readability.

# Variable names follow the same convention as function names.

# mixedCase is allowed only in contexts where that's already the prevailing
# style (e.g. threading.py), to retain backwards compatibility.

def func_greeting():
    """This is the example for function and variable names
    """
    print("Hello, This is my function")

# Function and method arguments

# Always use self for the first argument to instance methods.

# Always use cls for the first argument to class methods

# If a function argument's name clashes with a reserved keyword, it is generally
# better to append a single trailing underscore rather than use an abbreviation
# or spelling corruption. Thus class__ is better than clss.


class MyClassTwo(object):
    """This is the example for instance/class methods
    """

    def __init__(self, value):
        self.value = value

    @classmethod
    def greeting(cls):
        """This a class method.
        """
        print("Hello, Class method")

    def donothing(self, something):
        """This is a instance method.
        """
        if something != self.value:
            print("do nothing")
        else:
            print("do something")

# Method Names and Instance Variables

# Use the function naming rules: lowercase with words separated by underscores
# as necessary to improve readability.

# Use one leading underscore only for non-public methods and instance variables.

# To avoid name clashes with subclasses, use two leading underscores to invoke
# Python's name mangling rules.


# Constants

# Constants are usually defined on a module level and written in all capital
# letters with underscores separating words. Examples include MAX_OVERFLOW
# and TOTAL.

CONSTANTS_VAR = "This is a constant variable."

# Public and internal interfaces

# Any backwards compatibility guarantees apply only to public interfaces.
# Accordingly, it is important that users be able to clearly distinguish
# between public and internal interfaces.

# Documented interfaces are considered public, unless the documentation
# explicitly declares them to be provisional or internal interfaces exempt
# from the usual backwards compatibility guarantees. All undocumented
# interfaces should be assumed to be internal.

# To better support introspection, modules should explicitly declare the
# names in their public API using the __all__ attribute. Setting __all__
# to an empty list indicates that the module has no public API.

# Even with __all__ set appropriately, internal interfaces (packages,
# modules, classes, functions, attributes or other names) should still
# be prefixed with a single leading underscore.

# An interface is also considered internal if any containing namespace
# (package, module or class) is considered internal.

# Imported names should always be considered an implementation detail.
# Other modules must not rely on indirect access to such imported names
# unless they are an explicitly documented part of the containing module's
# API, such as os.path or a package's __init__ module that exposes
# functionality from submodules.

class MyClassThree(object):
    """This is the example for public and internal interface
    """

    def __init__(self, value):
        self.value = value

    def _internal_method(self, val):
        """This is a example for class internal method.
        """
        return self.value == val

    def public_method(self, val):
        """This is a example for class public method.
        """
        return self.value == val * 2


# https://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions
# https://www.python.org/dev/peps/pep-3131
# https://www.python.org/dev/peps/pep-0484
