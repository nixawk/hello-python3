#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
enum - Enumeration Type

The enum module defines an enumeration type with iteration and comparison capabilities. It can be used
to create well-defined symbols for values, instead of using literal integers or strings.
"""

import enum


class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

# The members of the Enum are converted to instances as the class is parsed. Each instance has a name property
# corresponding to the member name and a value property corresponding to the value assigned to the name in the
# class definition.

print('\nMember name: {}'.format(BugStatus.wont_fix.name))
print('Member value: {}'.format(BugStatus.wont_fix.value))


## References
# https://pymotw.com/3/enum/index.html