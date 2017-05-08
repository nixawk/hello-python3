#!/usr/bin/python
# -*- coding: utf-8 -*-

# The weakref module supports weak references to objects. A normal reference increments the reference
# count on the object and prevents it from being garbage collected. This outcome is not always desirable,
# especially when a circular reference might be present or when a cache of objects should be deleted when
# memory is needed. A weak reference is a handle to an object that does not keep it from being cleaned up
# automatically.

import weakref


class OriginalObject(object):

    def __del__(self):
        print('(Deleting {})'.format(self))


obj = OriginalObject()
ref = weakref.ref(obj)

print('obj: ', obj)
print('ref: ', ref)
print('ref(): ', ref())

print('deleting obj')
del obj
print('ref(): ', ref())