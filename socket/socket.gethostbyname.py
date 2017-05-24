#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket


print(socket.gethostbyname('www.python.org'))

"""
gethostbyname() to consult the operating system hostname resolution API and convert the name of
a server to its numerical address.

For accessing to more name information about a server, use gethostbyname_ex(). It returns the canonical
hostname of the server, any aliases, and all of the available IP addresses that can be used to reach it.
"""

# name, aliases, addresses = socket.gethostbyname_ex('www.python.org')
print(socket.gethostbyname_ex('www.python.org'))