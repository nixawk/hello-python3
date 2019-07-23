#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pika


def callback(ch, method, properties, body):
    """ Consumer callback functions.
    """
    print("[*] %r" % body)


def recv():
    """ Recv messages from queues.
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()
    channel.exchange_declare(exchange='logs', exchange_type='fanout')
    result = channel.queue_declare(
        queue='',  # create a queue with a random name
        exclusive=True  # once the consumer connection is closed, the queue should be deleted.
    )
    queue_name = result.method.queue
    channel.queue_bind(exchange='logs', queue=queue_name)

    channel = connection.channel()
    channel.basic_consume(
        queue=queue_name,
        on_message_callback=callback,
        auto_ack=True
    )

    channel.start_consuming()


if __name__ == '__main__':
    recv()

# https://www.rabbitmq.com/tutorials/tutorial-three-python.html
