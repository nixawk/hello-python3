#!/usr/bin/python
# -*- coding: utf-8 -*-

# Recursion

# One way to describe repetition within a computer program is the use of loops,
# such as Python's while-loop and for-loop constructs described. An entirely
# different way to achieve repetition is through a process known as recursion.

# Recursion is a technique by which a function makes one or more calls to
# itself during execution, or by which a data structure relies upon smaller
# instances of the very same type of structure in its representation.

# Recursion is an important technique in the study of data structure and
# algorithms.

# The Factorial Function

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# A recursion trace closely mirrors the programming language's execution of
# the recursion. In Python, each time a function (recursive or otherwise)
# is called, a structure known as an activation record or frame is created
# to store information about the progress of that invocation of the function.


if __name__ == '__main__':
    value = factorial(5)
    print(value)
