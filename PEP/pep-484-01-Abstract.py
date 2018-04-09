#!/usr/bin/python
# -*- coding: utf-8 -*-

# Abstract

# This PEP introduces a provisional module to provide these standard
# definitions and tools, along with some conventions for situations
# where annotations are not available.

def greeting(name: str) -> str:
	return "Hello " + name

# When these annotations are available at runtime through the usual
# __annotations__ attribute, no type checking happens at runtime.
# Instead.

# The type system supports unions, generic types, and a special type
# named Any which is consistent with all types.

if __name__ == '__main__':
	welcome = greeting('Python')
	print(welcome)

# Type Checking
# $ mypy pep-484-01-Abstract.py

## References
# https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep526
# https://www.python.org/dev/peps/pep-0484/
# https://www.python.org/dev/peps/pep-3107
# https://www.python.org/dev/peps/pep-0333