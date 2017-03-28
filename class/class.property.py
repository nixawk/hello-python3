#!/usr/bin/python
# -*- coding: utf-8 -*-


class MyClass(object):
    def __init__(self):
        super(MyClass, self).__init__()

    @property
    def name(self):
        return 'hello python'


if __name__ == '__main__':
    mc = MyClass()
    print(mc.name)
