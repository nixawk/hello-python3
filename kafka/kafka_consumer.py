#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from kafka import KafkaConsumer


consumer = KafkaConsumer('HelloKafka', bootstrap_servers='localhost:9092')
for msg in consumer:
    print(msg)
    print(msg.value)

# ConsumerRecord(topic='HelloKafka', partition=0, offset=10, timestamp=1559144103214, timestamp_type=0, key=None, value=b'This is a test message ', headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=23, serialized_header_size=-1)

# references
# https://zookeeper.apache.org/doc/r3.3.3/zookeeperStarted.html
# https://kafka.apache.org/quickstart
# https://www.tutorialspoint.com/apache_kafka/apache_kafka_basic_operations.htm
