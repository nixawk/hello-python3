#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# random.SystemRandom
# Alternate random number generator using sources provided by the operating
# system (such as /dev/urandom on Unix or CryptGenRandom on Windows).

# Not available on all systems (see os.urandom() for details).

import os
import random
import secrets


def os_urandom():
    print([os.urandom(5) for _ in range(5)])


def random_SystemRandom():
    cryptogen = random.SystemRandom()
    print([cryptogen.random() for _ in range(5)])


def secrets_randbelow():
    print([secrets.randbelow(5) for _ in range(5)])


if __name__ == '__main__':
    os_urandom()
    random_SystemRandom()
    secrets_randbelow()


# references
# https://stackoverflow.com/questions/20936993/how-can-i-create-a-random-number-that-is-cryptographically-secure-in-python