#!/usr/bin/env python
import pika
import sys


def send():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )
    channel = connection.channel()
    channel.exchange_declare(
        exchange='topic_logs',
        exchange_type='topic'
    )

    # Topic exchange

    # Messages sent to a topic exchange can't have an arbitrary routing_key - it
    # must be a list of words, delimited by dots. There can be as many words in
    # routing key as you like, up to the limit of 255 bytes.

    # * (star) can substitute for exactly one word.
    # # (hash) can substitute for zero or more words.

    routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
    message = ' '.join(sys.argv[2:]) or 'Hello World!'
    channel.basic_publish(
        exchange='topic_logs',
        routing_key=routing_key,
        body=message
    )
    print("[*] Sent %r:%r" % (routing_key, message))
    connection.close()


if __name__ == '__main__':
    send()

# https://www.rabbitmq.com/tutorials/tutorial-five-python.html