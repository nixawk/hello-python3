#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
hashlib.blake2b(
    data=b'', *,
    digest_size=64,
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

data: initial chunk of data to hash, which must be bytes-like object.
      It can be passed only as positional argument.

digest_size: size of output digest in bytes.

key: key for keyed hashing (up to 64 bytes for BLAKE2b, up to 32 bytes for BLAKE2s).

salt: salt for randomized hashing (up to 16 bytes for BLAKE2b, up to 8 bytes for BLAKE2s).

person: personalization string (up to 16 bytes for BLAKE2b, up to 8 bytes for BLAKE2s).

    Hash    digest_size len(key)    len(salt)   len(person)
    BLAKE2b 64          64          16          16
    BLAKE2s 32          32          8           8

fanout: fanout (0 to 255, 0 if unlimited, 1 in sequential mode).

depth: maximal depth of tree (1 to 255, 255 if unlimited, 1 in sequential mode).

leaf_size: maximal byte length of leaf (0 to 2**32-1,
           0 if unlimited or in sequential mode).

node_offset: node offset (0 to 2**64-1 for BLAKE2b, 0 to 2**48-1 for BLAKE2s,
             0 for the first, leftmost, leaf, or in sequential mode).

node_depth: node depth (0 to 255, 0 for leaves, or in sequential mode).

inner_size: inner digest size (0 to 64 for BLAKE2b, 0 to 32 for BLAKE2s,
            0 in sequential mode).

last_node: boolean indicating whether the processed node is the last one
           (False for sequential mode).

"""

import hashlib


def hashlib_blake2b_const():
    print(hashlib.blake2b.MAX_DIGEST_SIZE)  # 64
    print(hashlib.blake2b.MAX_KEY_SIZE)     # 64
    print(hashlib.blake2b.SALT_SIZE)        # 16
    print(hashlib.blake2b.PERSON_SIZE)      # 16


def hashlib_blake2b():
    data = "helloworld"
    print(hashlib.blake2b(data.encode()).hexdigest())
    print(hashlib.blake2b(data.encode(), digest_size=32).hexdigest())

    # print(
    #     hashlib.blake2b(
    #         data.encode(),
    #         digest_size=64,
    #         key='01234567'.encode() * 4,
    #         salt='01234567'.encode(),
    #         person='01234567'.encode()
    #     ).hexdigest()
    # )

    """
    Traceback (most recent call last):
      File "hashlib.blake2b.py", line 63, in <module>
        hashlib_blake2b()
      File "hashlib.blake2b.py", line 57, in hashlib_blake2b
        person='01234567'.encode()
    ValueError: digest_size must be between 1 and 64 bytes
    """


if __name__ == '__main__':
    hashlib_blake2b_const()
    hashlib_blake2b()

# references
# https://docs.python.org/3/library/hashlib.html#hashlib.blake2b
# https://github.com/python/cpython/tree/master/Modules/_blake2
