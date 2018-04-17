#!/usr/bin/python
# -*- coding: utf-8 -*-

import secrets


# secrets.token_hex([nbytes=None])

# Return a random text string, in dexadecimal. The string has nbytes random
# bytes, each byte converted to two hex digits. If nbytes is None or not
# supplied, a reasonable default is used.

print(secrets.token_hex(16))

# https://docs.python.org/3/library/secrets.html