#!/usr/bin/python3
# -*- coding: utf-8 -*-

import itertools


if __name__ == '__main__':
    counter = itertools.count()
    for i in range(100):
        next(counter)
    print(counter)
