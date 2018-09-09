#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct


def struct_Struct():
    mystruct = struct.Struct("<h")
    data_pack = mystruct.pack(0x0102)
    data_unpack = mystruct.unpack(data_pack)

    print(data_pack)  # b'\x02\x01'
    print("0x%(data)04x" % {'data': data_unpack[0]})  # 0x0102


if __name__ == '__main__':
    struct_Struct()


# reference
# https://docs.python.org/3.7/library/struct.html#struct.Struct