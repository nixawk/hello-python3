#!/usr/bin/python
# -*- coding: utf-8 -*-

# Problem

# You have code that accesses list or tuple elements by position, but this
# makes the code somewhat difficult to read at times. You'd also like to
# be less dependent on position in the structure, by accessing the elements
# by name.

# Solution

# collections.namedtuple() provides these benefits, while adding minimal
# overhead over using a normal tuple object. collections namedtuple() is
# actually a factory method that returns a subclass of the standard
# Python tuple type.

from collections import namedtuple


Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('test@example.com', '2012-10-19')

print(sub)
print(sub.addr)
print(sub.joined)
