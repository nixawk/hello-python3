#!/usr/bin/python
# -*- coding: utf-8 -*-

class ClassMethod_VS_StaticMethod(object):

    def method(self, value):
        """Here we have __init__, a typical initializer of Python class instances,
        which receives arguments as a typical instancemethod,
        having the first non-optional argument (self) that holds reference to a newly created instance.
        """
        print('hello %s' % value)

    @classmethod
    def class_method(cls, value):
        """the class of the object instance is implicitly passed as the first argument instead of self.
        """
        print('execute class_method(%s, %s)' % (cls, value))

    @staticmethod
    def static_method(value):
        """neither self (the object instance) nor  cls (the class) is implicitly passed as the first argument.
        They behave like plain functions except that you can call them from an instance or the class:
        """
        print('execute static_method(%s)' % value)


if __name__ == '__main__':
    ClassMethod_VS_StaticMethod.static_method('demostr')

    cvs = ClassMethod_VS_StaticMethod()
    cvs.class_method('demostr')


"""
$ python class.classmethod_VS_staticmethod.py
execute static_method(demostr)
execute class_method(<class '__main__.ClassMethod_VS_StaticMethod'>, demostr)
"""


## References

# https://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
# https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner