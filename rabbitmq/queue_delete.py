#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pika


def delete_queue(queue_name):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )

    channel = connection.channel()
    channel.queue_delete(queue_name)
    connection.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("[*] python %s <queue_name>" % sys.argv[0])
        sys.exit(1)

    delete_queue(sys.argv[1])

# https://github.com/pika/pika/blob/32de741f8d860982c6c8bc37d633ad78c16b630b/pika/channel.py#L849
