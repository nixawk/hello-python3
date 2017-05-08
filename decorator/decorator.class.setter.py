#!/usr/bin/python
# -*- coding: utf-8 -*-

from functools import wraps


class Person(object):

    age = property()

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @age.getter
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @classmethod
    def hello_classmethod(cls, string):
        print("classmethod says: 'hello {}'".format(string))

    @staticmethod
    def hello_staticmethod(string):
        print("staticmethod says: 'hello {}'".format(string))

    def hello_decorator(self, func):
        wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper


if __name__ == '__main__':
    p = Person('Jack', 25)
    print(p.name)
    print(p.age)

    p.hello_classmethod("python classmethod")
    p.hello_staticmethod("python staticmethod")