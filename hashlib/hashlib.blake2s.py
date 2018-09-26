#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
hashlib.blake2s(
    data=b'', *,
    digest_size=32,
    key=b'',
    salt=b'',
    person=b'',
    fanout=1,
    depth=1,
    leaf_size=0,
    node_offset=0,
    node_depth=0,
    inner_size=0,
    last_node=False
)

    Hash    digest_size len(key)    len(salt)   len(person)
    BLAKE2b 64          64          16          16
    BLAKE2s 32          32          8           8

"""

# hashlib.blake2s.MAX_DIGEST_SIZE
# hashlib.blake2s.MAX_KEY_SIZE
# hashlib.blake2s.SALT_SIZE
# hashlib.blake2s.PERSON_SIZE

import hmac
import hashlib


def hashlib_blake2s_const():
    print(hashlib.blake2s.MAX_DIGEST_SIZE)  # 32
    print(hashlib.blake2s.MAX_KEY_SIZE)     # 32
    print(hashlib.blake2s.SALT_SIZE)        # 8
    print(hashlib.blake2s.PERSON_SIZE)      # 8


def hashlib_blake2s():
    key = "privatekey"
    data = "helloworld"
    hmac_obj = hmac.new(
        key.encode(),
        msg=data.encode(),
        digestmod=hashlib.blake2s
    )
    print(hmac_obj.hexdigest())


if __name__ == '__main__':
    hashlib_blake2s_const()
    hashlib_blake2s()


# references
# http://blake2.net/
# https://docs.python.org/3/library/hashlib.html#hashlib.blake2b
# https://github.com/python/cpython/tree/master/Modules/_blake2