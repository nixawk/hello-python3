#!/usr/bin/python
# -*- coding: utf-8 -*-

from ctypes import *
import socket
import struct


class IP(Structure):

    _fields_ = [
        ("ihl", c_uint8, 4),
        ("version", c_uint8, 4),
        ("tos", c_uint8),
        ("len", c_uint16),
        ("id", c_uint16),
        ("offset", c_uint16),
        ("ttl", c_uint8),
        ("protocol_num", c_uint8),
        ("sum", c_uint16),
        ("src", c_uint32),
        ("dst", c_uint32)
    ]

    def __new__(self, buffer=None):
        # The problem is that from_buffer_copy creates new Structure instance
        # fron the given buffer. When you use it inside __init__, the Structure
        # has already been created and thus there would be no way to make use of
        # from_buffer_copy (and this is why only available as a class method),
        # not an instance method.
        return self.from_buffer_copy(buffer)

    def __init__(self, buffer=None):
        print(self.ihl.__hex__())
        print(self.version.__hex__())
        print(self.tos.__hex__())
        print(self.len.__hex__())
        print(self.id.__hex__())
        # print(struct.pack('<H', self.len))
        # print(struct.pack('<H', self.id))
        print(self.offset.__hex__())
        print(self.ttl.__hex__())
        print(self.protocol_num.__hex__())
        print(self.sum.__hex__())
        print(socket.inet_ntoa(struct.pack('<L', self.src)))
        print(socket.inet_ntoa(struct.pack('<L', self.dst)))

    def convert_bytes_to_structure(self, st, byte):
        memmove(addressof(st), byte, sizeof(st))

    def convert_struct_to_bytes(self, st):
        buffer = create_string_buffer(sizeof(st))
        memmove(buffer, addressof(st), sizeof(st))
        return buffer.raw


if __name__ == '__main__':
    buffer = 'E\x00\x00T\xd2\xce@\x00@\x01i\xd8\x7f\x00\x00\x01\x7f\x00\x00\x01'
    ip = IP(buffer)

    buffer2 = ip.convert_struct_to_bytes(ip)
    print(repr(buffer2))


## References
# ValueError: Buffer size too small (20 instead of at least 32 bytes)
# The problem is with 32 vs 64 bit systems.
# http://stackoverflow.com/questions/29306747/python-sniffing-from-black-hat-python-book
# http://stackoverflow.com/questions/1825715/how-to-pack-and-unpack-using-ctypes-structure-str
# https://gist.github.com/lmyyao/355709b35b717c9e47c6795de7b45ccd
