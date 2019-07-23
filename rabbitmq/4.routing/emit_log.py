#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pika


def send():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()
    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

    severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
    message = ' '.join(sys.argv[2:]) or 'Hello World!'
    channel.basic_publish(
        exchange='direct_logs',
        routing_key=severity,
        body=message
    )
    print("[*] Sent %r:%r" % (severity, message))
    connection.close()


if __name__ == '__main__':
    send()


# https://www.rabbitmq.com/tutorials/tutorial-four-python.html