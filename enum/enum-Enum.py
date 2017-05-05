#!/usr/bin/python3
# -*- coding: utf-8 -*-

import enum


# To require all members to have unique values, add the @unique decorator to the Enum.
@enum.unique
class BugStatus(enum.Enum):
    date = '2017-05-04'
    info = 'vulnerability information'


if __name__ == '__main__':
    for status in BugStatus:
        print('{} = {}'.format(status.name, status.value))

    # print(BugStatus.info.value)
    # print(BugStatus.date.value)