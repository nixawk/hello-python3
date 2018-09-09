#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
struct.pack(format, v1, v2, ...)

Return a bytes object containing the values v1, v2, ... packed according to the
format string format. The arguments must match the values required by the format
exactly.

Byte Order, Size, and Alignment

    @    native
    =    native
    <    little-endian
    >    big-endian
    !    network (= big-endian)

Format Characters

    x    pad byte
    c    char
    b    signed char
    B    unsigned char
    ?    _Bool
    h    short
    H    unsigned short
    i    int
    I    unsigned int
    l    long
    L    unsigned long
    q    long long
    Q    unsigned long long
    n    ssize_t
    N    size_t
    e    (7)
    f    float
    d    double
    s    char[]
    p    char[]
    P    void *
"""

import struct


def struct_pack():
    print(struct.pack('@bbbb', 0x1, 0x2, 0x3, 0x4))
    print(struct.pack('=bbbb', 0x1, 0x2, 0x3, 0x4))
    print(struct.pack('<bbbb', 0x1, 0x2, 0x3, 0x4))
    print(struct.pack('>bbbb', 0x1, 0x2, 0x3, 0x4))
    print(struct.pack('!bbbb', 0x1, 0x2, 0x3, 0x4))


if __name__ == '__main__':
    struct_pack()

# reference
# https://docs.python.org/3.7/library/struct.html