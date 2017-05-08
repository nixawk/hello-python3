#!/usr/bin/python
# -*- coding: utf-8 -*-

class Person(object):

    def __init__(self, name):
        self._name = name

    # Create a property instance
    name = property()

    @name.getter
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._name = value


if __name__ == '__main__':
    p = Person("Linux OS")
    print(p.name)