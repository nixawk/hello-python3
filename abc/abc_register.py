#!/usr/bin/python
# -*- coding: utf-8 -*-

import abc
from abc_base import PluginBase


class LocalBaseClass:
    pass


@PluginBase.register
class RegisteredImplementation(LocalBaseClass):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)


if __name__ == '__main__':
    print('Subclass:', issubclass(RegisteredImplementation, PluginBase))
    print('Instance:', isinstance(RegisteredImplementation(), PluginBase))

"""
$ python abc_register.py
Subclass: True
Instance: True
"""

"""
In this example the RegisteredImplementation is derived from LocalBaseClass, but is registered
as implementing the PluginBase API so issubclass() and isinstance() treat it as through it is
derived from PluginBase.
"""