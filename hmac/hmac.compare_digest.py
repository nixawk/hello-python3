#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
hmac.compare_digest(a, b)

Return a == b. This function uses an approach designed to prevent timing
analysis by avoiding content-based short circuiting behaviour, making it
appropriate for cryptography. a and b must both be of the same type: either
str (ASCII only, as e.g. returned by HMAC.hexdigest()), or a bytes-like object.
"""

import hmac
import hashlib


key = "keystring"
msg = "this is a demo string"


def hmac_new():
    hmac_obj = hmac.new(
        key.encode(),
        msg=msg.encode(),
        digestmod=hashlib.sha512
    )
    return hmac_obj.digest()


def hmac_digest():
    return hmac.digest(
        key.encode(),
        msg.encode(),
        hashlib.sha512
    )


if __name__ == '__main__':
    print(hmac.compare_digest(hmac_new(), hmac_digest()))


# reference
# https://docs.python.org/3/library/hmac.html#hmac.compare_digest