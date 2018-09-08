#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
textwrap.shorten(text, width, **kwargs)

Collapse and truncate the given text to fit in the given width.

irst the whitespace in text is collapsed (all whitespace is
replaced by single spaces). If the result fits in the width,
it is returned. Otherwise, enough words are dropped from the
end so that the remaining words plus the placeholder fit
within width:
"""

import textwrap


def textwrap_shorten():
    data = "This is a demo string."
    print(textwrap.shorten(data, width=16))                     # This is a [...]
    print(textwrap.shorten(data, width=16, placeholder="..."))  # This is a...


if __name__ == '__main__':
    textwrap_shorten()


# reference
# https://docs.python.org/3.7/library/textwrap.html
