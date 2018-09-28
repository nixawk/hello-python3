#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
class PrivateKey(encoding.Encodable, StringFixer, object):
    """
    Private key for decrypting messages using the Curve25519 algorithm.

    .. warning:: This **must** be protected and remain secret. Anyone who
        knows the value of your :class:`~nacl.public.PrivateKey` can decrypt
        any message encrypted by the corresponding
        :class:`~nacl.public.PublicKey`

    :param private_key: The private key used to decrypt messages
    :param encoder: The encoder class used to decode the given keys

    :cvar SIZE: The size that the private key is required to be
    :cvar SEED_SIZE: The size that the seed used to generate the
                     private key is required to be
    """

    SIZE = nacl.bindings.crypto_box_SECRETKEYBYTES
    SEED_SIZE = nacl.bindings.crypto_box_SEEDBYTES

    def __init__(self, private_key, encoder=encoding.RawEncoder):
        # Decode the secret_key
        private_key = encoder.decode(private_key)
        # verify the given secret key type and size are correct
        if not (isinstance(private_key, bytes) and
                len(private_key) == self.SIZE):
            raise exc.TypeError(("PrivateKey must be created from a {0} "
                                 "bytes long raw secret key").format(self.SIZE)
                                )

        raw_public_key = nacl.bindings.crypto_scalarmult_base(private_key)

        self._private_key = private_key
        self.public_key = PublicKey(raw_public_key)
'''

from nacl.public import PrivateKey
from nacl.utils import random


def nacl_public_PrivateKey():
    key1 = PrivateKey(random(size=PrivateKey.SIZE))  # 32
    print(key1.encode())

    key2 = PrivateKey.generate()
    print(key2.encode())


if __name__ == '__main__':
    nacl_public_PrivateKey()

# reference
# https://pynacl.readthedocs.io/en/stable/public/#nacl.public.PrivateKey