#!/usr/bin/python
# -*- coding: utf-8 -*-

# Normal Lock objects cannot be acquired more than once, even by the same thread.
# This can introduce undersirable side-effects if a lock is accessed by more than
# one function in the same call chain.

import threading

lock = threading.RLock()

print('First try :', lock.acquire())
print('Second try :', lock.acquire(0))