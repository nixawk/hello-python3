#!/usr/bin/python
# -*- coding: utf-8 -*-

import secrets


# secrets.token_urlsafe([nbytes=None])

# Return a random URL-safe text string, containing nbytes random bytes.
# The text is Base64 encoded, so on average each byte results in approximately
# 1.3 characters. If nbytes is None or not supplied, a reasonable default is
# used.

print(secrets.token_urlsafe(16))

# https://docs.python.org/3/library/secrets.html