#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Code objects are used by the implementation to represent "pseudo-compiled"
executable Python code such as a function body. They differ from function
objects because they don't contain a reference to their global execution
environment. Code objects are returned by the built-in compile() function
and can be extracted from function objects through their __code__ attribute.

A code object can be executed or evaluated by passing it (instead of a source
string) to the exec() or eval() built-in functions.

----

compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1

Compile source into a code object that can be executed by exec() or eval().

The source code may represent a Python module, statement or expression.
The filename will be used for run-time error messages.
The mode must be 'exec' to compile a module, 'single' to compile a
single (interactive) statement, or 'eval' to compile an expression.
The flags argument, if present, controls which future statements influence
the compilation of the code.
The dont_inherit argument, if true, stops the compilation inheriting
the effects of any future statements in effect in the code calling
compile; if absent or false these statements do influence the compilation,
in addition to any features explicitly specified.
"""

filename = 'str.capitalize.py'
source = open(filename).read()
code_object = compile(source, filename, 'exec')
exec(code_object)
