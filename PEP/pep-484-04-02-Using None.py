#!/usr/bin/python
# -*- coding: utf-8 -*-

# Using None

# When used in a type hint, the expression None is considered
# equivalent to type(None).

def test() -> None:
    pass


if __name__ == '__main__':
    test()


# https://www.python.org/dev/peps/pep-0484/#using-none