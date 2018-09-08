#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def bytes_decode():
    data = u'Hello россия'

    bytes_data = bytes(data, encoding='utf-8')
    data_encode = data.encode(encoding='utf-8')

    print(bytes_data)            # b'Hello \xd1\x80\xd0\xbe\xd1\x81\xd1\x81\xd0\xb8\xd1\x8f'
    print(data_encode)           # b'Hello \xd1\x80\xd0\xbe\xd1\x81\xd1\x81\xd0\xb8\xd1\x8f'
    print(data_encode.decode())  # Hello россия


if __name__ == '__main__':
    bytes_decode()


# reference
# https://docs.python.org/3.7/library/stdtypes.html#bytes.decode