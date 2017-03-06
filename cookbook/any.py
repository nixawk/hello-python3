#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os


files = os.listdir('/tmp/')
if any(name.endswith('.py') for name in files):
    print('There be python.')
else:
    print('Sorry, no python.')
