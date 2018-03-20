#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib import parse


print(parse.unquote('http://www.example.com/?id=1%20+%202'))