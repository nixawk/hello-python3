#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from contextvars import (
    ContextVar,
    Token
)


def main():
    var: ContextVar[int] = ContextVar('var', default=42)
    token = var.set(100)

    assert isinstance(token, Token), Exception("not Token instance")

    print(token.var.get())
    print(token.old_value)
    var.reset(token)
    print(var.get())


if __name__ == '__main__':
    main()


# references
# https://docs.python.org/3/library/contextvars.html#contextvars.contextvars.Token