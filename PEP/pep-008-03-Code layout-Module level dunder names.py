#!/usr/bin/python
# -*- coding: utf-8 -*-

"""This is the example module.

This module does stuff.
"""

from __future__ import barry_as_FLUFL

# Module level "dunders" such as __all__, __author__, __version__, etc.
# should be placed after the module docstring but before any import
# statements except from __future__ imports. Python mandates that
# future-imports must appear in the module before any other code
# except docstrings.

__all__ = [
    'MyClass',
    'myfunc'
]
__version__ = '0.1'
__author__ = 'pep8'
__license__ = 'Python License'


class MyClass(object):
    """This is the example class.
    """

    def __init__(self, value):
        self.value = value

    def dowhat(self):
        """This is a example func in class."""
        return self.value

    @classmethod
    def greeting(cls):
        """This is my greeting func.
        """
        print("Hello Python")


def myfunc():
    """This is a example func"""
    return "Hello, Python"


if __name__ == '__main__':
    MYCLS = MyClass('Python')
    MYCLS.dowhat()

# https://www.python.org/dev/peps/pep-0008/#module-level-dunder-names
# https://www.python.org/dev/peps/pep-0401/
# https://stackoverflow.com/questions/4007289/so-what-exactly-does-from-future-import-barry-as-flufl-do/4007310?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
# https://stackoverflow.com/questions/2674035/how-to-handle-the-pylint-message-warning-method-could-be-a-function?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
