#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from contextvars import (
    ContextVar,
    copy_context
)


def create_context():
    name: ContextVar[str] = ContextVar('name', default='katz')
    age: ContextVar[int] = ContextVar('age', default=25)

    name.set('Tim')
    age.set(28)


def main():
    create_context()

    ctx: Context = copy_context()
    print(list(ctx.items()))


if __name__ == '__main__':
    main()


"""
$ py3 contextvars.copy_context.py
[(<ContextVar name='name' default='katz' at 0x102384ca8>, 'Tim'), (<ContextVar name='age' default=25 at 0x1028673b8>, 28)]
"""

# references
# https://docs.python.org/3/library/contextvars.html#manual-context-management
