#!/usr/bin/python
# -*- coding: utf-8 -*-

# Problem

# You want to keep a limited history of the last few items seen during
# iteration or during some other kind of processing.

# Solution

# Keeping a limited history is a perfect use for a collections.deque.

from collections import deque


def show_deque_limit(iterator, history=5):

    # Using deque(maxlen=N) creates a fixed-sized queue. When new items are
    # added and the queue is full, the oldest item is automatically removed.

    previous_items = deque(maxlen=history)
    for item in iterator:
        previous_items.append(item)
        print(previous_items)


if __name__ == '__main__':
    iterator = range(9)
    show_deque_limit(iterator)


"""
$ python3 self.py
deque([0], maxlen=5)
deque([0, 1], maxlen=5)
deque([0, 1, 2], maxlen=5)
deque([0, 1, 2, 3], maxlen=5)
deque([0, 1, 2, 3, 4], maxlen=5)
deque([1, 2, 3, 4, 5], maxlen=5)
deque([2, 3, 4, 5, 6], maxlen=5)
deque([3, 4, 5, 6, 7], maxlen=5)
deque([4, 5, 6, 7, 8], maxlen=5)
"""