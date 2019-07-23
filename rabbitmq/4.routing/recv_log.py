#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pika


def callback(ch, method, properties, body):
    """ Consumer callback function.
    """
    print("[*] Recv: %r:%r" % (method.routing_key, body))


def recv():
    """ Receives messages from queues.
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()
    channel.exchange_declare(
        exchange='direct_logs',
        exchange_type='direct'
    )

    result = channel.queue_declare(
        queue='',
        exclusive=True,  # Only allow access by the current connection,
        auto_delete=True # Delete after consumer cancels or disconnects
    )
    queue_name = result.method.queue

    severities = sys.argv[1:]
    if not severities:
        sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
        sys.exit(1)

    for severity in severities:
        channel.queue_bind(
            exchange='direct_logs',
            queue=queue_name,
            routing_key=severity
        )

    print('[*] Waiting for logs. To exit press CTRL+C')

    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )

    channel.start_consuming()


if __name__ == '__main__':
    recv()

# https://www.rabbitmq.com/tutorials/tutorial-four-python.html
# https://github.com/pika/pika/blob/master/pika/channel.py#L784
