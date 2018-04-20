#!/usr/bin/python
# -*- coding: utf-8 -*-

# Conditional Expressions

# Python supports a conditional expression syntax that can replace a simple
# control structure. The general syntax is an expression of the form:

    # expr1 is condition else expr2

INT_A = 1
STR_A = "C" if INT_A > 0 else "Python"

print(STR_A)

# Sometimes, the mere shortening of source code is advantageous because it
# avoids the distraction of a more cumbersome control structure. However,
# we recommend that a conditional expression be used only when it improves
# the readability of the source code.
