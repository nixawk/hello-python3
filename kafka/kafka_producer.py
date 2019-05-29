#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='localhost:9092')
for _ in range(10):
    msg = bytes("This is the %d message" % _, "utf-8")
    print(msg)
    producer.send('HelloKafka', msg)

producer.flush()

# references
# https://zookeeper.apache.org/doc/r3.3.3/zookeeperStarted.html
# https://kafka.apache.org/quickstart
# https://www.tutorialspoint.com/apache_kafka/apache_kafka_basic_operations.htm
