#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
class PublicKey(encoding.Encodable, StringFixer, object):
    """
    The public key counterpart to an Curve25519 :class:`nacl.public.PrivateKey`
    for encrypting messages.

    :param public_key: [:class:`bytes`] Encoded Curve25519 public key
    :param encoder: A class that is able to decode the `public_key`

    :cvar SIZE: The size that the public key is required to be
    """

    SIZE = nacl.bindings.crypto_box_PUBLICKEYBYTES

    def __init__(self, public_key, encoder=encoding.RawEncoder):
        self._public_key = encoder.decode(public_key)
        if not isinstance(self._public_key, bytes):
            raise exc.TypeError("PublicKey must be created from 32 bytes")

        if len(self._public_key) != self.SIZE:
            raise exc.ValueError(
                "The public key must be exactly {0} bytes long".format(
                    self.SIZE
                )
            )

    def __bytes__(self):
        return self._public_key

    def __hash__(self):
        return hash(bytes(self))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return nacl.bindings.sodium_memcmp(bytes(self), bytes(other))

    def __ne__(self, other):
        return not (self == other)
File:           ~/Library/Python/3.6/lib/python/site-packages/nacl/public.py
Type:           type
'''

from nacl.public import PublicKey
from nacl.utils import random
from nacl.encoding import Base64Encoder
import base64


def nacl_public_PublicKey():
    bytes32 = random(size=32)

    print(len(bytes32))

    pubkey1 = PublicKey(bytes32)
    pubkey2 = PublicKey(base64.b64encode(bytes32), encoder=Base64Encoder)

    print(pubkey1.encode())
    print(pubkey2.encode())

    # b'\xcb{\x1eA\x13\xf4\xcd@\xf7\xd3\xf1\x82\x973q\xc6U\xe4Z\xa10\x98\x06I\x123Z:\x1f\xe9\x0fm'


if __name__ == '__main__':
    nacl_public_PublicKey()

# reference
# https://pynacl.readthedocs.io/en/stable/public/#nacl.public.PublicKey
