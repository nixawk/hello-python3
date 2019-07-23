#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sudo rabbitmqctl list_exchanges
# sudo rabbitmqctl list_bindings

# Deliver a message to multiple consumers, this pattern is known as
# "publish/subscribe"


import sys
import pika


def send():
    """ Send messages into exchanges.
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters("localhost")
    )
    channel = connection.channel()

    # The core idea in the messaging model in RabbitMQ is that the producer
    # never sends any messages directly to a queue. Actually, quite often 
    # the producer doesn't even know if a message will be delivered to any
    # queue at all.

    # Instead, the producer can only send messages to an exchange. 

    # There are a few exchange types available:

        # direct
        # topic
        # headers
        # fanout 

    # The fanout exchange just broadcasts all the messages it receives to all
    # the queue it knowns.

    channel.exchange_declare(
        exchange='logs',
        exchange_type='fanout'
    )
    message = ' '.join(sys.argv[1:]) or "info: Hello World!"
    channel.basic_publish(
        exchange='logs',
        routing_key='',  # Temporary queues
        body=message
    )
    connection.close()


if __name__ == '__main__':
    send()


# https://www.rabbitmq.com/tutorials/tutorial-three-python.html
