#!/usr/bin/python
# -*- coding: utf-8 -*-

import abc
from abc_base import PluginBase


@PluginBase.register
class IncompleteImplementation(PluginBase):

    def save(self, output, data):
        return output.write(data)


if __name__ == '__main__':
    print('Subclass:', issubclass(IncompleteImplementation, PluginBase))
    print('Instance:', isinstance(IncompleteImplementation(), PluginBase))


"""
$ python abc_incomplete.py
Subclass: True
Traceback (most recent call last):
  File "abc_incomplete.py", line 17, in <module>
    print('Instance:', isinstance(IncompleteImplementation(), PluginBase))
TypeError: Can't instantiate abstract class IncompleteImplementation with abstract methods load
"""

"""
Another benefit of subclassing directly from the abstract base class is that the subclass cannot
be instantiated unless it fully implements the abstract portion of the API.
"""