#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
class threading.Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)


threading.Thread.start
threading.Thread.run
threading.Thread.join
threading.Thread.name
threading.Thread.getName
threading.Thread.setName
threading.Thread.ident
threading.Thread.is_alive
threading.Thread.daemon
threading.Thread.isDaemon
threading.Thread.setDaemon
"""

from __future__ import print_function
from __future__ import unicode_literals

import threading


class MyThread(threading.Thread):

    def __init__(self, *args, **kwargs):
        super(MyThread, self).__init__(*args, **kwargs)

    def run(self):
        print("called by threading.Thread.start()")

        # def start(self):
        #     _start_new_thread(self._bootstrap, ())

        # def _bootstrap(self):
        #     self._bootstrap_inner()

        # def _bootstrap_inner(self):
        #     self.run()


if __name__ == '__main__':
    mythread = MyThread()
    mythread.start()
    mythread.join()

# References
# https://docs.python.org/3/library/threading.html#threading.Thread
# https://github.com/python/cpython/blob/master/Lib/threading.py#L854
# https://stackoverflow.com/questions/23224784/start-vs-run-for-threads-in-python

