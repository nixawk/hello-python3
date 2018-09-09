#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
class enum.Enum
    Base class for creating enumerated constants. See section
    Functional API for an alternate construction syntax.


enum.unique()
    Enum class decorator that ensures only one name is bound to any one value.
"""

import enum


@enum.unique
class Module(enum.Enum):
    name        = 'Cisco RCE Exploit'
    description = '...'
    author      = 'Cisco'
    license     = 'GPL3'
    references  = [
        'https://www.example.com/exploits/xxxxx',
        'https://www.example.com/exploits/yyyyy',        
    ]
    date        = '2017-05-04'


def enum_Enum():
    for _ in dir(Module):
        if _.startswith('__'):
            continue

        mod = getattr(Module, _)
        print('%(name)16s: %(value)s' % {
            'name': mod.name,
            'value': mod.value,
        })


if __name__ == '__main__':
    enum_Enum()


"""
$ python3 enum-Enum.py
          author: Cisco
            date: 2017-05-04
     description: ...
         license: GPL3
            name: Cisco RCE Exploit
      references: ['https://www.example.com/exploits/xxxxx', 'https://www.example.com/exploits/yyyyy']
"""


# reference
# https://docs.python.org/3/library/enum.html
# https://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python
