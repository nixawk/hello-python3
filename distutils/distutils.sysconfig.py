#!/usr/bin/python
# -*- coding: utf-8 -*-

import distutils.sysconfig


"""
distutils.sysconfig

    Provide access to Python's configuration information. The specific
    configuration variables depend heavily on the platform and configuration.
"""

print(distutils.sysconfig.get_python_lib())
print(distutils.sysconfig.get_python_version())
