#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
hmac.new(key, msg=None, digestmod=None)

Return a new hmac object.
key is a bytes or bytearray object giving the secret key.
If msg is present, the method call update(msg) is made. 
digestmod is the digest name, digest constructor or module
for the HMAC object to use. It supports any name suitable
to hashlib.new() and defaults to the hashlib.md5 constructor.

Changed in version 3.4: Parameter key can be a bytes or bytearray
object. Parameter msg can be of any type supported by hashlib.
Parameter digestmod can be the name of a hash algorithm.

Deprecated since version 3.4, will be removed in version 3.8: MD5
as implicit default digest for digestmod is deprecated.
"""

import hmac
import hashlib


def hmac_new():
    key = "keystring"
    msg = "this is a demo string"
    hmac_obj = hmac.new(   # hamc.HMAC()
        key.encode(),
        msg=msg.encode(),
        digestmod=hashlib.sha512
    )

    print(hmac_obj.hexdigest())  # 8f2a0e31bad23cf255fa0e6d77b5d4f2577b252d061d983b0a152101c590e91bb7229aa3b818a8a28ad21f711aa5c0a5699411d6e22bcb74d4bc95f8ed1c9e76
    print(hmac_obj.digest())     # b'\x8f*\x0e1\xba\xd2<\xf2U\xfa\x0emw\xb5\xd4\xf2W{%-\x06\x1d\x98;\n\x15!\x01\xc5\x90\xe9\x1b\xb7"\x9a\xa3\xb8\x18\xa8\xa2\x8a\xd2\x1fq\x1a\xa5\xc0\xa5i\x94\x11\xd6\xe2+\xcbt\xd4\xbc\x95\xf8\xed\x1c\x9ev'
    print(hmac_obj.name)         # hmac-sha512
    print(hmac_obj.digest_size)  # 64
    print(hmac_obj.block_size)   # 128


if __name__ == '__main__':
    hmac_new()


# reference
# https://docs.python.org/3/library/hmac.html
