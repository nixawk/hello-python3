#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64
import random


def base64_encode(data):
    """ Base16, Base32, Base64, Base85 Data Encodings.
    """
    return (
        base64.b64encode(data),
        base64.a85encode(data),
        base64.b85encode(data)
    )


if __name__ == '__main__':
    fmt = "%4s %4s %4s"
    print(fmt % ("b64", "a85", "b85"))
    print(fmt % ("===", "===", "==="))

    for i in range(100):
        b64, a85, b85 = base64_encode(i * b"A")
        print(fmt % (len(b64), len(a85), len(b85)))


# references
# https://docs.python.org/3/library/base64.html
