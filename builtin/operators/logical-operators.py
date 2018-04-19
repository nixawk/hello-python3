#!/usr/bin/python
# -*- coding: utf-8 -*-

# Logical Operators

# Python supports the following keyword operators for Boolean values:

    # not  unary negation
    # and  conditional and
    # or   conditional or

# The [and] and [or] operators short-circuit, in that they do not evaluate
# the second operand if the result can be determined based on the value of
# the first operand. This feature is useful when constructing Boolean
# expressions in which we first test that a certain condition holds (such as
# reference not being None), and then test a condition that could have
# otherwise generated an error condition had the prior test not successed.

print(1 not in range(5))
print(2 > 1 and 3 > 2)
print(2 > 1 or 2 > 3)

