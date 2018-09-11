#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
hmac.digest(key, msg, digest)

Return digest of msg for given secret key and digest.
The function is equivalent to HMAC(key, msg, digest).digest(),
but uses an optimized C or inline implementation, which is
faster for messages that fit into memory. The parameters key,
msg, and digest have the same meaning as in new().

CPython implementation detail, the optimized C implementation
is only used when digest is a string and name of a digest algorithm,
which is supported by OpenSSL.
"""

import hmac
import hashlib


def hmac_digest():
    key = "keystring"
    msg = "this is a demo string"
    hmac_digest_data = hmac.digest(
        key.encode(),
        msg.encode(),
        hashlib.sha256
    )

    print(hmac_digest_data)  # b'\xe6B\x97a\x9b\rYgI\xe51\x0f\xffP\xfa\xcc\xba#\xefk?\xbbi\xa8\x8b\x88g\x1d-\xf7\x14_'


if __name__ == '__main__':
    hmac_digest()


# reference
# https://docs.python.org/3/library/hmac.html
