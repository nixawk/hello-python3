#!/usr/bin/python3
# -*- coding: utf-8 -*-

import secrets


def main():
    # Return a random int in range [0, n).
    print(secrets.randbelow(10))

    # Generates an int with k random bits.
    # (111, 110, 101, 011, 100, 010, 001, 010, 000)
    k = 3
    print(secrets.randbits(k))

    # Return a random byte string containing *nbytes* bytes.
    nbytes = 6
    print(secrets.token_bytes(nbytes))

    # Return a random text string, in hexadecimal
    # The string has *nbytes* random bytes, each byte converted to two
    # hex digits. If *nbytes* is ``None`` or not supplied,
    # a reasonable defult is used.
    nbytes = 16
    print(secrets.token_hex(nbytes))

    # Return a random URL-safe text string, in Base64 encoding.
    # The string has *nbytes* random bytes. If *nbytes* is ``None``
    # or not supplied, a reasonable default is used.
    nbytes = 16
    print(secrets.token_urlsafe(nbytes))

if __name__ == "__main__":
    main()
