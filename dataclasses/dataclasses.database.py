#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass


@dataclass
class PERSON(object):
    name: str
    age: int
    uid: int

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_uid(self):
        return self.uid


if __name__ == '__main__':
    person = PERSON(name='katz', age=25, uid=1000)
    print(person.get_name())


# references
# https://docs.python.org/3/library/dataclasses.html#module-dataclasses