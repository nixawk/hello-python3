#!/usr/bin/python
# -*- coding: utf-8 -*-

from ctypes import *


libc = CDLL("libc.so.6")
libc.printf("helloworld\n")
