#!/usr/bin/python
# -*- coding: utf-8 -*-

import abc


class PluginBase(abc.ABC):

    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source and return an object.
        """

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output.
        """


class SubclassImplementation(PluginBase):

    def load(self, input):
        return input.read()

    def save(self, output, data):
        return output.write(data)


if __name__ == '__main__':
    print('Subclass:', issubclass(SubclassImplementation, PluginBase))
    print('Instance:', isinstance(SubclassImplementation(), PluginBase))


"""
$ python abc_abc_base.py
Subclass: True
Instance: True
"""