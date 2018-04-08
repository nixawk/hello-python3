#!/usr/bin/python
# -*- coding: utf-8 -*-

# PEP 498, formatted string literals.

# Formatted string literals are prefixed with 'f' and are similar to the
# format strings accepted by str.format(). They contain replacement fields
# surrounded by curly braces. The replacement fields are expressions, which
# are evaluated at run time, and then formatted using the format() protocol.

# In source code, f-strings are string literals that are prefixed by the letter
# 'f' or 'F'. Everyone this PEP uses 'f', 'F' may also be used.
# 'f' may be combined with 'r' or 'R', in either order, to produce raw f-string
# literals. 'f' may not be combined with 'b': this PEP does not propose to add
# binary f-strings. 'f' may not be combined with 'u'.

# Python supports multiple ways to format text strings. These include
# 1. %-formatting
# 2. str.format()
# 3. string.Template
# 4. literal string interpolation
# Each of these methods have their advantages, but in addition have disadvantage
# that make them cumbersome to use in practice.


# 1. %-formatting
# %-formatting is limited as to the types it supports. Only ints, strs, and
# doubles can be formatted. All other types are either not supported, or converted
# to one of these types before formatting. In addition, there's a well-known trap
# where a single value is passed.

# f' <text> { <expression> <optional !s, !r, or !a> <optional : format specifier> }'

from datetime import datetime
from decimal import Decimal


def simple_usage():
    # normal usage for literal string interpolation

    def format_int():
        integer = 4
        print(f"int = {integer}")
        print(f"int = {integer:#08x}")
        print(f"int = {integer}")


    def format_str():
        language = "Python"
        print(f"str = Hello, {language}")
        print(f"str = Hello, {language!s}")    # '!s' calls str() on the expression 
        print(f"str = Hello, {language!r}")    # '!r' calls repr() on the expression
        print(f"str = Hello, {language!a}")    # '!a' calls ascii() on the expression
        print(f"str = Hello, {language:1.2}")  # Format specifiers


    def format_date():
        now = datetime.now()
        print(f"date = {now:%A, %B, %d, %Y}")


    def format_func():
        print(f"func = {globals()}")

    format_int()
    format_str()
    format_date()
    format_func()


def escape_sequences():
    # Backslashes may not appear inside the expression portions of f-strings,
    # so you cannot use them, for example, to escape quotes inside f-strings
    welcome = "Hello, Python"
    # print(f'{\'welcome\'}')  # SyntaxError: f-string expression part cannot include a backslash
    print(f"{'welcome'}")      # escape
    print(f"{{globals()}}")


def code_equivalence():
    # The exact code used to implement f-strings is not specified. However, it
    # is guaranteed that any embedded value that is converted to a string will use that
    # value's __format__ method. This is the same mechanism that str.format() uses to
    # convert values to strings.
    txt = "Hello, C"
    print(f"{txt!r} and Python is my favorite")


def expression_evaluation():
    # The expression that are extracted from the string are evaluated in the context
    # where the f-string appeared. This means the expression has full access to local
    # abd global variables. Any valid Python expression can be used, including function and
    # method calls.
    print(f"{globals()}")


def format_specifiers():
    # Format specifiers may also contain evaluated expressions,
    width = 10
    precision = 4
    value = Decimal('12.34567')
    print(f'result: {value:{width}.{precision}}')


def concatenating_strings():
    # Adjacent f-strings and regular strings are concatenated. Regular strings are concatenated
    # at compile time, and f-strings are concatenated at run time.
    language = 'Python'
    print(
        'Hello,'
        'C'
        ' and '
       f'{language}'
    )

def error_handing():
    # Either compile time or run time errors can occur when processing f-strings. Compile time
    # errors are limited to these errors that can be detected when scanning an f-string. These
    # errors all raise
    print(f"{raise_an_exception}")


if __name__ == '__main__':

    simple_usage()

    escape_sequences()
    code_equivalence()
    expression_evaluation()
    format_specifiers()
    concatenating_strings()
    error_handing()

# https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498
# https://www.python.org/dev/peps/pep-0498/