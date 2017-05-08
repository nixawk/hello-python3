#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle
import io


class ClassOne(object):

	def __init__(self):
		data = {'author': 'python', 'cve': '2080-1100'}

	def hello(self):
		print("hello python")


pickle_dump_data = io.BytesIO()
pickle.dump(ClassOne, pickle_dump_data)
pickle_dump_data.flush()

print(pickle_dump_data.getvalue())

pickle_load_data = io.BytesIO(pickle_dump_data.getvalue())

print(pickle.load(pickle_load_data))


## References

# https://docs.python.org/3/library/pickle.html
# https://pymotw.com/3/pickle/index.html
