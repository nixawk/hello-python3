#!/usr/bin/python
# -*- coding: utf-8 -*-

from functools import wraps, partial
import logging


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    """Add logging to a function. level is the logging level,
    name is the logger name, and message is the log message.
    If name and message aren't specified, they default to the function's module and name.
    """

    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwds):
        log.log(level, logmsg)
        return func(*args, **kwds)
    return wrapper


@logged()
def add(x, y):
    return x + y


@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')


if __name__ == '__main__':
    add(1, 2)
    spam()