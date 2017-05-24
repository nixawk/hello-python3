#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python supports three address families. The most common, AF_INET, is used for IPv4 Internet addressing.
IPv4 addresses are four bytes long and are usually represented as a sequence of four numbers, one per octet,
separated by dots (e.g., 10.1.1.5 and 127.0.0.1). These values are more commonly referred to as “IP addresses.
” Almost all Internet networking is done using IP version 4 at this time.

AF_INET6 is used for IPv6 Internet addressing. IPv6 is the “next generation” version of the Internet protocol,
and supports 128-bit addresses, traffic shaping, and routing features not available under IPv4. Adoption of
IPv6 continues to grow, especially with the proliferation of cloud computing and the extra devices being added
to the network because of Internet-of-things projects.

AF_UNIX is the address family for Unix Domain Sockets (UDS), an inter-process communication protocol available
on POSIX-compliant systems. The implementation of UDS typically allows the operating system to pass data directly
from process to process, without going through the network stack. This is more efficient than using AF_INET,
but because the file system is used as the namespace for addressing, UDS is restricted to processes on the same system.
The appeal of using UDS over other IPC mechanisms such as named pipes or shared memory is that the programming interface
is the same as for IP networking, so the application can take advantage of efficient communication when running on a single host,
but use the same code when sending data across the network.
"""

import contextlib
import socket


def socket_AF_INET():
    with contextlib.closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as client:
        client.settimeout(8)
        client.connect(('www.python.org', 80))
        client.send(b'GET / HTTP/1.1\r\nHost: www.python.org\r\n\r\n')
        print(client.recv(1024))


def socket_AF_INET6():
    # https://stackoverflow.com/questions/5358021/establishing-an-ipv6-connection-using-sockets-in-python
    with contextlib.closing(socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)) as client:
        client.connect(('2a04:4e42:15::223', 80, 0, 0))
        client.send(b'GET / HTTP/1.1\r\nHost: www.python.org\r\n\r\n')
        print(client.recv(1024))


if __name__ == '__main__':
    socket_AF_INET()
    socket_AF_INET6()