#!/usr/bin/python
# -*- coding: utf-8 -*-

import secrets


# secrets.choice(sequence)

# Return a randomly-chosen element from a non-empty sequence

languages = ['C', 'C++', 'Python', 'Ruby', 'Go', 'Shell']

for _ in range(5):
    print(secrets.choice(languages))

"""
$ python3 secrets-choice.py
C++
Shell
Go
Ruby
Ruby
"""

# https://docs.python.org/3/library/secrets.html