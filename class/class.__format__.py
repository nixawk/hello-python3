#!/usr/bin/python
# -*- coding: utf-8 -*-

class Date(object):

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

        self.formats = {
            'ymd': '{d.year}-{d.month}-{d.day}',
            'mdy': '{d.month}/{d.day}/{d.year}',
            'dmy': '{d.day}/{d.month}/{d.year}'
        }

    def __format__(self, code):
        code = code if code else 'ymd'
        fmt = self.formats[code]
        return fmt.format(d=self)


if __name__ == '__main__':
    dt = Date(2017, 5, 4)
    print(format(dt))
    print(format(dt, 'mdy'))
    print(format(dt, 'dmy'))