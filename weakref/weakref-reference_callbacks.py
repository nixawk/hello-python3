#!/usr/bin/python
# -*- coding: utf-8 -*-

## Reference Callbacks

# The ref constructor accepts an optional callback function that is invoked when the referenced object is deleted.

import weakref


class OriginalObject(object):

    def __del__(self):
        print('(Deleting {})'.format(self))


def callback(reference):
	"""Invoke when 
	"""
	print('callback{!r}'.format(reference))


obj = OriginalObject()
ref = weakref.ref(obj, callback)

print('obj: ', obj)
print('ref: ', ref)
print('ref(): ', ref())

print('deleting obj')
del obj
print('ref(): ', ref())

# The callback receives the reference object as an argument after the reference is "dead" and no longer
# refers to the original object. One use for this feature is to remove the weak reference object froma a cache.