#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cProfile


def demo():
    print(sum([_ for _ in range(1000000)]))


if __name__ == '__main__':
    cProfile.run("demo()")


"""
$ py3 cProfile.run.py
499999500000
         7 function calls in 0.068 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.067    0.067 <string>:1(<module>)
        1    0.009    0.009    0.067    0.067 cProfile.run.py:7(demo)
        1    0.049    0.049    0.049    0.049 cProfile.run.py:8(<listcomp>)
        1    0.000    0.000    0.068    0.068 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.009    0.009    0.009    0.009 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
