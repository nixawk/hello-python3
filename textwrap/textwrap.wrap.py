#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
textwrap.wrap(text, width=70, **kwargs)

Wraps the single paragraph in text (a string) so every line
is at most width characters long. Returns a list of output
lines, without final newlines.

Optional keyword arguments correspond to the instance
attributes of TextWrapper, documented below. width defaults to 70.
"""

import textwrap


def textwrap_wrap():
    data = "Wraps the single paragraph in text (a string) so every line is at most width characters long. Returns a list of output lines, without final newlines."
    print("\n".join(textwrap.wrap(data, width=79)))


if __name__ == '__main__':
    textwrap_wrap()


# reference
# https://docs.python.org/3.7/library/textwrap.html