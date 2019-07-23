#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# rabbitmqctl list_bindings

import sys
import pika


def callback(ch, method, properties, body):
    """ Consumer callback function.
    """
    print("[*] Recv: %r:%r" % (method.routing_key, body))


def recv():
    """ Receives messages from queue.
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()

    channel.exchange_declare(
        exchange='topic_logs',
        exchange_type='topic'
    )

    result = channel.queue_declare(
        '',
        exclusive=True
    )
    queue_name = result.method.queue

    binding_keys = sys.argv[1:]
    if not binding_keys:
        sys.stderr.write("Usage: %s [binding_key]...\n" % sys.argv[0])
        sys.exit(1)

    for binding_key in binding_keys:
        channel.queue_bind(
            exchange='topic_logs',
            queue=queue_name,
            routing_key=binding_key
        )

    print(' [*] Waiting for logs. To exit press CTRL+C')

    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )

    channel.start_consuming()


if __name__ == '__main__':
    recv()

# https://www.rabbitmq.com/tutorials/tutorial-five-python.html
