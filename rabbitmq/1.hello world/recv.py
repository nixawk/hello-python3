#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Please keep in mind that this and other tutorials are, well, tutorials. They
# demonstrate one new concept at a time and may intentionally oversimplify some 
# things and leave out others. For example topics such as connection management,
# error handling, connection recovery, concurrency and metric collection are
# largely omitted for the sake of brevity. Such simplified code should not be 
# considered production ready.


import pika


def callback(ch, method, properties, body):
    print("[*] Received %r" % body)


def recv():
    """ Receives messages from the queue.
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost')
    )
    channel = connection.channel()
    channel.basic_consume(
        queue='hello',
        auto_ack=True,
        on_message_callback=callback
    )
    channel.start_consuming()


if __name__ == '__main__':
    recv()

# https://www.rabbitmq.com/tutorials/tutorial-one-python.html
