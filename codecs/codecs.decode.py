#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
codecs.decode(obj, encoding='utf-8', errors='strict')

Decodes obj using the codec registered for encoding.

Errors may be given to set the desired error handling
scheme. The default error handler is 'strict' meaning
that decoding errors raise ValueError (or a more codec
specific subclass, such as UnicodeDecodeError). Refer
to Codec Base Classes for more information on codec
error handling.
"""

import codecs


def codecs_decode():
    print(codecs.decode(b'hello world', encoding="utf-8"))
    print(codecs.decode(b'hello \xd1\x80\xd0\xbe\xd1\x81\xd1\x81\xd0\xb8\xd1\x8f', encoding="utf-8"))


if __name__ == '__main__':
    codecs_decode()


# reference
# https://docs.python.org/3.7/library/codecs.html