#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ecdsa



def sign_and_verify():
    """demo for private key/public key sign/verify.
    """
    sk = ecdsa.SigningKey.generate(ecdsa.SECP256k1)  # sign key
    vk = sk.get_verifying_key()                      # verify key

    msg = b'hello, ecdsa'
    sig = sk.sign(msg)
    assert(vk.verify(sig, msg))

    vk = ecdsa.VerifyingKey.from_string(
        vk.to_string(),
        curve=ecdsa.SECP256k1
    )
    assert(vk.verify(sig, msg))

    print({
        'private_key': bytes.hex(sk.to_string()),
        'public_key': bytes.hex(vk.to_string()),
        'msg': msg,
        'sig': bytes.hex(sig)
    })


if __name__ == '__main__':
    sign_and_verify()


# references
# https://stackoverflow.com/questions/34451214/how-to-sign-and-verify-signature-with-ecdsa-in-python
# https://crypto.stackexchange.com/questions/14662/using-ecdsa-keys-for-encryption
# https://bitcoin.stackexchange.com/questions/53375/online-tool-to-play-around-with-ecdsa-public-keys-message-signature-verificatio