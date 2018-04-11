#!/usr/bin/python
# -*- coding: utf-8 -*-

# Comments

# Comments that contradict the code are worse than no comments. Always make
# a priority of keeping the comments up-to-date when code changes!

# Comments should be complete sentences. The first word should be captialized,
# unless it is an identifier that begins with a lower case letter (never
# alter the case of identifier!).

# Block Comments

# Block comments generally apply to some (or all) code that follows them, and
# are indented to the same level as that code. Each line of a block comment
# starts with a # and a single space (unless it is indented text inside the
# ccomment).

def show_block_comments():
    """This is the example function.
    """
    print("This is Block Comments")

# Inline Comments

# Using inline comments sparingly.
# An inline comment is a comment on the same line as a statement. Inline
# comments should be separated by at least two spaces from the statement.
# They should start with a # and a single space.

show_block_comments()
print("This is inline comments")  # inline comments

# Documentation Strings

# Conventations for writing good documentation strings are immortallzed in
# PEP 257.

# Write docstrings for all public modules, functions, classes, and methods.
# Docstrings are not necessary for non-public methods, but you should have
# a comment that describes what the method does. This comment should appear
# after the def line.

# PEP 257 describes good docstring conventions. Note that most importantly,
# the """ that ends a multiline docstring should be on a line by itself,

# For one liner docstrings, please keep the closing """ on the same line.

# https://www.python.org/dev/peps/pep-0008/#comments
# https://www.python.org/dev/peps/pep-0257
