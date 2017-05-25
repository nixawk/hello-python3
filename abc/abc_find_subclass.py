#!/usr/bin/python
# -*- coding: utf-8 -*-

import abc
from abc_base import PluginBase
import abc_subclass
import abc_register


for sc in PluginBase.__subclasses__():
    print(sc.__name__)


"""
$ python abc_find_subclass.py
SubclassImplementation
"""

"""
Even through abc_register() is imported, RegisteredImplementation is not among the list of subclass
because it is not actually derived from the base.
"""