#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
struct.unpack(buffer)

Identical to the unpack() function, using the compiled format.
The buffer’s size in bytes must equal size.

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


def struct_unpack():
    data = b'\x01\x02\x03\x04\x05\x06\x07\x08'
    print(hex(struct.unpack("<q", data)[0]))  # 0x807060504030201
    print(hex(struct.unpack(">q", data)[0]))  # 0x102030405060708

    print(struct.calcsize("x"))  # 1
    print(struct.calcsize("c"))  # 1
    print(struct.calcsize("b"))  # 1
    print(struct.calcsize("B"))  # 1
    print(struct.calcsize("?"))  # 1
    print(struct.calcsize("h"))  # 2
    print(struct.calcsize("H"))  # 2
    print(struct.calcsize("i"))  # 4
    print(struct.calcsize("I"))  # 4
    print(struct.calcsize("l"))  # 8
    print(struct.calcsize("L"))  # 8
    print(struct.calcsize("q"))  # 8
    print(struct.calcsize("Q"))  # 8
    print(struct.calcsize("n"))  # 8
    print(struct.calcsize("N"))  # 8
    print(struct.calcsize("e"))  # 2
    print(struct.calcsize("f"))  # 4
    print(struct.calcsize("d"))  # 8
    print(struct.calcsize("s"))  # 1
    print(struct.calcsize("p"))  # 1
    print(struct.calcsize("P"))  # 8


if __name__ == '__main__':
    struct_unpack()


# reference
# https://docs.python.org/3.7/library/struct.html