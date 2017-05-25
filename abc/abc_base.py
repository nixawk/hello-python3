#!/usr/bin/python
# -*- coding: utf-8 -*-

import abc


class PluginBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def load(self, input):
        """Retrieve data from the input source and return an object.
        """
        pass

    @abc.abstractmethod
    def save(self, output, data):
        """Save the data object to the output.
        """
        pass