#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
textwrap.fill(text, width=70, **kwargs)

Wraps the single paragraph in text, and returns a single string containing
the wrapped paragraph. fill() is shorthand for

    "\n".join(wrap(text, ...))

"""

import textwrap


def textwrap_wrap():
    data = "Wraps the single paragraph in text (a string) so every line is at most width characters long. Returns a list of output lines, without final newlines."
    # print("\n".join(textwrap.wrap(data, width=79)))
    print(textwrap.join(data, width=79))


if __name__ == '__main__':
    textwrap_wrap()


# reference
# https://docs.python.org/3.7/library/textwrap.html