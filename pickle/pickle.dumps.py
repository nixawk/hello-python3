#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle


class ClassOne(object):

    def __init__(self):
        data = {'author': 'python', 'cve': '2080-1100'}

    def hello(self):
        print("hello python")


pickle_dumps_data = pickle.dumps(ClassOne)
pickle_loads_data = pickle.loads(pickle_dumps_data)

print(pickle_dumps_data)
print(pickle_loads_data)

classone = pickle_loads_data()
classone.hello()

# Uses dump() to encode a data structure as a string.

## Warning

# The documentation for pickle makes clear that it offers no security guarantees. In fact,
# unpickling data an execute arbitrary code. Be careful using pickle for inter-process
# communication or data storage, and do not trust data that cannot be verified as secure.

## References

# https://docs.python.org/3/library/pickle.html
# https://pymotw.com/3/pickle/index.html
