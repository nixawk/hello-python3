#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Proxies

It is sometimes more convenient to use a proxy, rather than a weak reference. Proxies can be used as though they
were the original object, and do not need to be called before the object is accessible. As a consequence, they
can be passed to a library that does not know it is receiving a reference instead of the real object.
"""

import weakref


class OriginalObject(object):

    def __init__(self, name):
    	self.name = name

    def __del__(self):
        print('(Deleting {})'.format(self))


obj = OriginalObject("Python-Object")
ref = weakref.ref(obj)
pxy = weakref.proxy(obj)

print('via obj:', obj.name)
print('via ref:', ref().name)
print('via proxy:', pxy.name)

del obj
print('via proxy:', pxy.name)