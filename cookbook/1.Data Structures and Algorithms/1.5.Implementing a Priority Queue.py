#!/usr/bin/python
# -*- coding: utf-8 -*-

# Problem

# You want to implement a queue that sorts items by a given priority and
# always returns the item with the highest priority on each pop operation.

# Solution

# The following class uses the heapq module to implement a simple priority
# queue.

import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):

        # The queue consists of tuples of the form (-priority, index, item).
        # The priority value is negated to get the queue to sort items from
        # highest priority to lowest priority. This is opposite of the normal
        # heap ordering, which sorts from lowest to highest value.

        # The role of the index variable is to properly order items with
        # the same priority level. By keeping a constantly increasing index,
        # the items will be sorted according to the order in which they were
        # inserted. However, the index also serves an important role in making
        # the comparison operations work for items that have the same priority
        # level.

        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.push(Item('foo'), 1)
    pq.push(Item('bar'), 5)
    pq.push(Item('spam'), 4)
    pq.push(Item('grok'), 1)

    print(pq.pop())
    print(pq.pop())
    print(pq.pop())
    print(pq.pop())


# >>> aa = Item('foo')
# >>> bb = Item('bar')
# >>> aa < bb
# *** TypeError: '<' not supported between instances of 'Item' and 'Item'

# >>> aa = (1, Item('foo'))
# >>> bb = (5, Item('bar'))
# >>> aa < bb
# True


# Discussion

# The core of this recipe concerns the use of the heapq module. The functions
# heapq.heappush() and heapq.pop() insert and remove items from a list _queue
# in a way such that the first item in the list has the smallest priority.
# The heappop() method always returns the "smallest" item, so that is the key
# to making the queue pop the ciorrect items. Moreover, since the push and pop
# opeartions have O (log N) complexity where N is the number of items in the
# heap, they are fairly effcient even for fairly large values of N.

# https://docs.python.org/3/library/heapq.html