#!/usr/bin/python
# -*- coding: utf-8 -*-

class ClassOne(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.classname = type(self).__name__

    def __repr__(self):  # obj = eval(repr(obj))
        return '{0.classname!s}({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)


if __name__ == '__main__':
    classone = ClassOne(1, 2)
    print(classone)
    print(repr(classone))