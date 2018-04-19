#!/usr/bin/python
# -*- coding: utf-8 -*-


# Generator

# Python's generators provide a convenient way to implement the iterator
# procotol. If a container object's __iter__() method is implemented as
# a generator, it will automatically return an iterator object (technically,
# a generator object) supplying the __iter__() and __next__() methods.
# More information about generators can be found in the documentation
# for the yield expression.

# A generator is implemented with a syntax that is very similar to a function,
# but instead of returning values, a yield statement is executed to indicate
# each element of the series.

# It is illegal to combine yield and return statements in the same
# implementation, other than a zero-agrument return statements to
# cause a generator to end its execution.


def declare_generator(iterator):
    for item in iterator:
        yield item


def multi_yield_generator():
    # Python executes our procedure until a yield statement indicates
    # the next value.
    yield "AAAA"
    yield "BBBB"
    yield "CCCC"
    yield "DDDD"


if __name__ == '__main__':
    for _ in declare_generator([1, 2, 3, 4, 5]):
        print(_)

    generator = multi_yield_generator()
    print(next(generator))  # output: AAAA
    print(next(generator))  # output: BBBB


# $ py3 generators.py
# 1
# 2
# 3
# 4
# 5
# AAAA

# https://wiki.python.org/moin/Generators
