#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pika


def exchange_delete(exchange_name):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )

    channel = connection.channel()
    channel.exchange_delete(exchange_name)
    connection.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("[*] python %s <exchange_name>" % sys.argv[0])
        sys.exit(1)

    exchange_delete(sys.argv[1])

# https://github.com/pika/pika/blob/32de741f8d860982c6c8bc37d633ad78c16b630b/pika/channel.py#L676
