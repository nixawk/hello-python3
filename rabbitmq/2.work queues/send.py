#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pika


def send():
    """ Send a single message to the queue.
    """
    message = ''.join(sys.argv[1:]) or "Hello World!"
    connection = pika.BlockingConnection(
        pika.ConnectionParameter("localhost")
    )
    channel = connection.channel()

    # When RabbitMQ quits or crashes it will forget the queues and messages
    # unless you tell it not to. Two things are required to make sure that
    # messages aren't lost; we need to mark both quene and messages as durable.
    channel.queue_declare(
        queue='hello',
        durable=True
    )
    channel.basic_publish(
        exchange='',
        routing_key='hello',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2, # make message persistent
        )
    )
    connection.close()


if __name__ == '__main__':
    send()


# https://www.rabbitmq.com/tutorials/tutorial-two-python.html