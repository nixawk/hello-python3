#!/usr/bin/python3
# -*- coding: utf-8 -*-

text = 'root:*:0:0:System Administrator:/var/root:/bin/sh'
username, *unuse, homedir, sh = text.split(':')

print(username)
print(homedir)
print(sh)

# Pleaes compare the following methods.
print(*unuse)
print(unuse)

# If it runs in python2, you will get:
# SyntaxError: invalid syntax
