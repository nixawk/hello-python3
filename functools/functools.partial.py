#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
## partial Objects

partial objects callable objects created by partial(). They have three read-only attributes:

partial.func

    A callable object or function. Calls to the partial object will be forwarded to func with new arguments and keywords.

partial.args

    The leftmost positional arguments that will be prepended to the positional argument provided to a partial object call.

partial.keywords

    The keyword arguments that will be supplied when the partial object is called.

partial objects are like function objects in that they are callable, weak referencable, and can have attributes.
There are some important differences. For instance, the __name__ and __doc__ attributes are not created automatically.
Also, partial objects defined in classes behave like static methods and do not transform into bound methods during
instance attribute look-up.
"""


from functools import partial


RECORD_SIZE = 32

with open('/etc/passwd', 'r') as f:
    """
    iter(iterable) -> iterator
    iter(callable, sentinel) -> iterator

    Get an iterator from an object.  In the first form, the argument must
    supply its own iterator, or be a sequence.
    """
    records = iter(partial(f.read, RECORD_SIZE), '')
    for record in records:
        print(record)
