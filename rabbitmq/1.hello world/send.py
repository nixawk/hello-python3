#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sudo rabbitmqctl list_queues

import pika


def send():
    """ Send a single message to the queue.
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )
    channel = connection.channel()

    # Create a queue. The commmand can be run as many times as we like,
    # and only one will be created.
    channel.queue_declare(queue='hello')
    channel.basic_publish(
        exchange='',
        routing_key='hello',  # quene name
        body='Hello World !'
    )
    
    # Before exiting the program we need to make sure the network buffers
    # were flushed and our message was delivered to RabbitMQ.
    connection.close()


if __name__ == '__main__':
    send()

# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
