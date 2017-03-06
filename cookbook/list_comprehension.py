#!/usr/bin/python3
# -*- coding: utf-8 -*-

# The easiest way to filter sequence data is often to use a list comprehension.
# One potential downside of using a list comprehension is that it might produce
# a large result if the original input is large. If this is a concern, you can
# use generator expressions to produce the filtered values iteratively.
mylist = [1, 4, -5, -10, -7, 2, 3, -1]
# a list
lst = [_ for _ in mylist if _ > 0]
print(lst)

# a generator
gen = (_ for _ in mylist if _ > 0)
print(gen)
