#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    assert os.path.exists(filename), Exception("File not found.")
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


def mmap_replace(filename, data):
    if isinstance(data, str):
        data = data.encode()

    with memory_map(filename) as m:
        datalen = len(data)
        memlen = len(m)

        if datalen <= memlen:
            m[0: datalen] = data
        else:
            m[0: memlen] = data[0: memlen]


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"[*] python {sys.argv[0]} filename filedata")
        sys.exit(1)

    mmap_replace(sys.argv[1], sys.argv[2])


# references
# https://docs.python.org/3.0/library/mmap.html
# https://stackoverflow.com/questions/34600452/python-mmap-replace-substitute-using-regex