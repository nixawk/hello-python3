#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading


def worker(num):
    """thread worker function"""
    print('Worker: %s' % num)


if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()