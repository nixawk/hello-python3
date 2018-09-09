#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
codecs.encode(obj, encoding='utf-8', errors='strict')

Encodes obj using the codec registered for encoding.

Errors may be given to set the desired error handling scheme.
The default error handler is 'strict' meaning that encoding
errors raise ValueError (or a more codec specific subclass,
such as UnicodeEncodeError). Refer to Codec Base Classes for
more information on codec error handling.
"""

import codecs


def codecs_encode():
    print(codecs.encode("hello world", encoding="utf-8"))  # b'hello world'
    print(codecs.encode("hello россия", encoding="utf-8")) # b'hello \xd1\x80\xd0\xbe\xd1\x81\xd1\x81\xd0\xb8\xd1\x8f'
    print(bytes("hello world", encoding="utf-8"))          # b'hello world'
    print(bytes("hello россия", encoding="utf-8"))         # b'hello \xd1\x80\xd0\xbe\xd1\x81\xd1\x81\xd0\xb8\xd1\x8f'


if __name__ == '__main__':
    codecs_encode()


# reference
# https://docs.python.org/3.7/library/codecs.html
