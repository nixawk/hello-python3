#!/usr/bin/python
# -*- coding: utf-8 -*-

# Callable

# Frameworks expecting callback functions of specific signatures might be
# type hinted using
# Callable[[Arg1Type, Arg2Type], ReturnType]

from typing import Callable
import logging


logging.basicConfig(level=logging.INFO)


def func_without_log() -> None:
    pass


def partial(func: Callable[[], None]) -> None:
    logging.info(func.__name__)


# Note that there are no square brackets around he ellipsis.
# The argument of the callback are completely unconstrained
# in this case (and keyword arguments are acceptable).

# Since using callbacks with keyword arguments is not perceived
# as a common use case, there is currently no support for
# specifying keyword arguments with Callable. Similarly,
# there is no support for specifying callback signatures with
# a variable number of argument of a specific type.

# Because typing.Callable does double-duty as a replacement
# for collections.abc.Callable, isinstance(x, typing.Callable)
# is implemented by deferring to isinstance(x, collections.abc.Callable).
# However, isinstance(x, typing.Callable[...]) is not supported.


if __name__ == '__main__':
    partial(func_without_log)


# https://www.python.org/dev/peps/pep-0484/#callable