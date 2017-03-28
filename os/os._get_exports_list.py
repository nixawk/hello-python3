#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys


"""
def _get_exports_list(module):
    try:
        return list(module.__all__)
    except AttributeError:
        return [n for n in dir(module) if n[0] != '_']
"""

print(os._get_exports_list(sys))
