#!/usr/bin/python
# -*- coding: utf-8 -*-


import socket


"""
To find the offcial name of the current host, use gethostname()
The name returned will depend on the network settings for the current system,
and may change if it is on a different nework (such as a laptop attached to a 
wireless LAN).
"""

print(socket.gethostname())