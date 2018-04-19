#!/usr/bin/python
# -*- coding: utf-8 -*-

# Break and Continue Statements

# Python supports a break statement that immediately terminate a while or for
# loop when executed within its body. More formally, if applied within nested
# control structures, it cause the termination of the most immediately
# enclosing loop.

print('demo for break')
for _ in range(5):
    if _ == 2:
        break
    print(_)


# Python also supports a continue statement that causes the current iteration
# of a loop body to stop, but with subsequent passes of the loop processding
# as expected.

print('demo for continue')
for _ in range(5):
    if _ == 2:
        continue
    print(_)
