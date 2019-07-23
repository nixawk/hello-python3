#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid
import pika


class FibonacciRpcClient(object):
    """ RabbitMQ RPC Client.
    """

    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='localhost')
        )

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True
        )

    def on_response(self, ch, method, props, body):
        """ Consumer callback function.
        """
        if self.corr_id == props.correlation_id:
            self.response = body

    def call(self, n):
        """ RPC Call.
        """
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties=pika.BasicProperties(
                reply_to=self.callback_queue,
                correlation_id=self.corr_id,
            ),
            body=str(n)
        )

        while self.response is None:
            self.connection.process_data_events()

        return int(self.response)


if __name__ == '__main__':
    print("[*] Client: Requesting fib(30)")
    print("[*] Client: Got %r" % FibonacciRpcClient().call(30))

# https://www.rabbitmq.com/tutorials/tutorial-six-python.html
