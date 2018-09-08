#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
bytes.count(sub[, start[, end]])¶
bytearray.count(sub[, start[, end]])

Return the number of non-overlapping occurrentces of subsequence
sub in the range [start, end]. Optional arguments start and end
are interpreted as in slice notation.

sub is a bytes-like-object.
"""

def bytes_count():
    data = "helloworld"
    print(bytes(data, encoding='utf-8').count(b'l', 0, len(data)))


if __name__ == '__main__':
    bytes_count()


# reference
# https://docs.python.org/3.7/library/stdtypes.html#bytes.count