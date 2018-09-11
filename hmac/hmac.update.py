#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
HMAC.update(msg)

Update the hmac object with msg. Repeated calls are equivalent to a single call
with the concatenation of all the arguments: m.update(a); m.update(b) is
equivalent to m.update(a + b).
"""

import hmac
import hashlib


def hmac_update():
    key = "keystring"
    msg = "this is a demo string"
    hamc_obj = hmac.new(key.encode(), digestmod=hashlib.sha512)
    hamc_obj.update(msg.encode())
    print(hamc_obj.hexdigest())  # 8f2a0e31bad23cf255fa0e6d77b5d4f2577b252d061d983b0a152101c590e91bb7229aa3b818a8a28ad21f711aa5c0a5699411d6e22bcb74d4bc95f8ed1c9e76


if __name__ == '__main__':
    hmac_update()

# reference
# https://docs.python.org/3/library/hmac.html