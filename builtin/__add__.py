#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass

@dataclass
class MYCLASS(object):

    total : int

    def __add__(self, cls):
        self.total += cls.total
        return self


if __name__ == '__main__':
    cls1 = MYCLASS(total=11)
    cls2 = MYCLASS(total=22)

    cls3 = cls1 + cls2
    print(cls3.total)


# references
# https://www.python.org/dev/peps/pep-3114/