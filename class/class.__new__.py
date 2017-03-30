#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Use __new__ when you need to control the creation of a new instance.
Use __init__ when you need to control initialization of a new instance.

__new__ is the first step of instance creation. It's called first, and is
responsible for returning a new instance of your class. In contrast,
__init__ doesn't return anything; it's only responsible for initializing the
instance after it's been created.

In general, you shouldn't need to override __new__ unless you're subclassing
an immutable type like str, int, unicode or tuple.

__new__ is called automatically when calling the class name (when instantiating),
whereas __init__ is called every time an instance of the class is returned by
__new__ passing the returned instance to __init__ as the 'self' parameter,
therefore even if you were to save the instance somewhere globally/statically
and return it every time from __new__, then __init__ will be called every time
you do just that.
"""


class MyClass(object):

    def __new__(self, *args, **kwds):
        print('__new__')
        return super(MyClass, self).__new__(self, *args, **kwds)

    def __init__(self, *args, **kwds):
        print('__init__')

    def helloworld(self):
        print("hello world")


class MyClass2(object):

    def __new__(self, *args, **kwds):
        print('__new__')

    def __init__(self):
        print('__init__')

    def helloworld(self):
        print("hello world")


myclass = MyClass()
myclass.helloworld()

myclass2 = MyClass2()
myclass2.helloworld()  # AttributeError: 'NoneType' object has no attribute 'helloworld'

## References
# https://mail.python.org/pipermail/tutor/2008-April/061426.html
# http://spyhce.com/blog/understanding-new-and-init
