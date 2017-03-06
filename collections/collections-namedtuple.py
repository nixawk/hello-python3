#!/usr/bin/python3
# -*- coding: utf-8 -*-

from collections import namedtuple


# One possible use of a namedtuple is as a replacement for a dictionary,
# which requires more space to store. Thus, if you are building large data
# structures involving dictionaries, use of a namedtuple will be more efficient
# . However, be aware that unlike a dictionary, a namedtuple is immutable.

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub.addr)
print(sub.joined)

_addr, _joined = sub
print(_addr)
print(_joined)

# If you need to change any of the attributes, it can be done using the
# _replace() method of a namedtuple instance, which makes an entirely
# new namedtuple with specified values replaced.

sub2 = sub._replace(addr='test@example.com')
print(sub)
print(sub2)
