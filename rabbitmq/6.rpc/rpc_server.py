#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pika


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body):
    n = int(body)

    print("[*] Server: fib(%s)" % n)
    response = fib(n)

    ch.basic_publish(
        exchange='',
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=str(response)
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


def recv():
    """ Receives messages from queue.
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost')
    )

    channel = connection.channel()
    channel.queue_declare(queue='rpc_queue')

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='rpc_queue', on_message_callback=on_request)

    print("[*] Awaiting RPC requests")
    channel.start_consuming()


if __name__ == '__main__':
    recv()

# https://www.rabbitmq.com/tutorials/tutorial-six-python.html
