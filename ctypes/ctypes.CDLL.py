#!/usr/bin/python
# -*- coding: utf-8 -*-

from ctypes import *


"""
#include <stdio.h>

void myprint(void);

void myprint()
{
    printf("hello world\n");
}

# *inx
$ gcc -shared -Wl,-soname,testlib -o testlib.so -fPIC testlib.c

# or... for Mac OS X
$ gcc -shared -Wl,-install_name,testlib.so -o testlib.so -fPIC testlib.c
"""

libc = CDLL("libc.so.6")
libc.printf("helloworld\n")


# https://docs.python.org/3.6/library/ctypes.html
# http://stackoverflow.com/questions/5081875/ctypes-beginner
