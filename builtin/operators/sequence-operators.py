#!/usr/bin/python
# -*- coding: utf-8 -*-

# Sequence Operators

# Each of Python's built-in sequence types (str, tuple, and list) support the
# following operator syntaxes:

    # s[j]                  element at index j
    # s[start:stop]         slice including indices [start, stop)
    # s[start:stop:step].   slice including indices start, start + step, start + 2 * step, ...,
    # s + t                 concatenation of sequences
    # k * s                 shorthand for s + s + s + ... (k times)
    # val in s              containment check
    # val not in s          non-containment check

LIST_A = [0, 1, 2, 3, 4]

print(LIST_A[0])
print(LIST_A[0:3])
print(LIST_A[0:3:2])

print("HELLO " * 2)
print("HELLO" in "HELLO, WORLD")    # True
print("PYTHON" in "HELLO, WORLD")   # False
