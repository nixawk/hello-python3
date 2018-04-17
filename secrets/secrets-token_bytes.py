#!/usr/bin/python
# -*- coding: utf-8 -*-

import secrets

# secrets.token_bytes([nbytes=None])

# Return a random byte string containing nbytes number of bytes. If nbytes
# is None or not supplied, a reasonable default is used.

print(secrets.token_bytes(16))

# https://docs.python.org/3/library/secrets.html