#!/usr/bin/python
# -*- coding: utf-8 -*-

# Comprehension Syntax

# A very common programming task is to produce one series of values based upon
# the processing of another series. Often, this task can be accomplished quite
# simply in Python using what is known as a comprehension syntax.


    # [k * k for k in range(1, n+1)]     # list comprehension
    # {k * k for k in range(1, n+1)}     # set comprehension
    # (k * k for k in range(1, n+1))     # generator comprehension
    # {k: k * k for k in range(1, n+1)}  # dictionary comprehension

LIST_A = [1, 2, 3, 4]

print(sum([k * 10 for k in LIST_A]))     # output: 100
print(sum({k * 10 for k in LIST_A}))     # output: 100
print(sum((k * 10 for k in LIST_A)))     # output: 100
