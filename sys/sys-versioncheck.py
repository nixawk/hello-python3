#!/usr/bin/python
# -*- coding: utf-8 -*-

# Version and platform checking

import sys


if sys.version_info[0] >= 3:
	print('Python 3 specific definitions')
else:
	print('Python 2 specific definitions')


if sys.platform == 'win32':
	print('Windows specific definitions')
else:
	print('Posix specific definitions')



## References
# https://www.python.org/dev/peps/pep-0484/