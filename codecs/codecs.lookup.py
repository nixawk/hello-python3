#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
codecs.lookup(encoding)

Looks up the codec info in the Python codec registry and returns
a CodecInfo object as defined below.

Encodings are first looked up in the registry’s cache. If not found,
the list of registered search functions is scanned. If no CodecInfo
object is found, a LookupError is raised. Otherwise, the CodecInfo
object is stored in the cache and returned to the caller.
"""

import codecs


def codecs_lookup():
    codec_info_obj = codecs.lookup('utf-8')
    print(codec_info_obj.name)
    print(codec_info_obj.encode("hello россия"))
    print(codec_info_obj.decode(b'hello \xd1\x80\xd0\xbe\xd1\x81\xd1\x81\xd0\xb8\xd1\x8f'))


if __name__ == '__main__':
    codecs_lookup()

# reference
# https://docs.python.org/3.7/library/codecs.html