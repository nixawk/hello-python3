#!/usr/bin/python
# -*- coding: utf-8 -*-


import select
import socket
import time


class EventHandler(object):

    def fileno(self):
        'Return the associated file descriptor'
        return NotImplemented('must implement')

    def wants_to_receive(self):
        'Return True if receiving is allowed'
        return False

    def handle_receive(self):
        'Perform the receive operation'
        pass

    def wants_to_send(self):
        'Return True if sending is requested'
        return False

    def handle_send(self):
        'Send outgoing data'
        pass


class UDPServer(EventHandler):

    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(address)

    def fileno(self):
        return self.sock.fileno()

    def wants_to_receive(self):
        return True


class UDPTimeServer(UDPServer):

    def handle_receive(self):
        msg, addr = self.sock.recvfrom(1)
        self.sock.sendto(time.ctime().encode('ascii'), addr)


class UDPEchoServer(UDPServer):

    def handle_receive(self):
        msg, addr = self.sock.recvfrom(8192)
        self.sock.sendto(msg, addr)


def event_loop(handlers):
    while True:
        wants_recv = [h for h in handlers if h.wants_to_receive()]
        wants_send = [h for h in handlers if h.wants_to_send()]
        can_recv, can_send, _ = select.select(wants_recv, wants_send, [])

        for h in can_recv: h.handle_receive()
        for h in can_send: h.handle_send()


if __name__ == '__main__':
    handlers = [UDPTimeServer(('', 14000)), UDPEchoServer(('', 15000))]
    event_loop(handlers)

"""
import socket

s.sendto(b'', ('localhost', 14000))
print(s.recvfrom(128))
s.sendto(b'hello', ('localhost', 15000))
print(s.recvfrom(128))
s.close()
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
"""

## References

# 1. Python3 Cookbook

