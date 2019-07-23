#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged

import time
import pika


def callback(ch, method, properties, body):
    """ Consumer callback function.
    """
    print("[*] Received %r" % body)
    time.sleep(body.count(b'.'))
    print("[*] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def recv():
    """ Receives messages from rabbitmq.
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameter("localhost")
    )
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    # You might have noticed that the dispatching still doesn't work exactly as
    # we want. For example in a situation with two workers, when all odd
    # messages are heavy and even messages are light. one worker will be
    # constantly busy and the other one will do hardly any work.
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(
        queue='hello',
        auto_ack=True,
        on_message_callback=callback
    )
    connection.close()


if __name__ == '__main__':
    recv()


# In order to make sure a message is never lost, Rabbitmq supports message
# acknowledgments. An ack(nowledgement) is sent back by the consumer to tell
# RabbitMQ that a particular message had been received, processed and that
# RabbitMQ is free to delete it.

# If a consumer dies (its channel is closed, connection is closed, or TCP
# connection is lost) without sending an ack, RabbitMQ will understand that
# a message wasn't processed fully and will re-queue it. If there are other
# consumers online at the same time, it will then quickly redeliver it to 
#another consumer. That way you can be sure that no message is lost, even
# if the workers occasionally die.

# https://www.rabbitmq.com/tutorials/tutorial-two-python.html