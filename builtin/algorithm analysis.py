#!/usr/bin/python
# -*- coding: utf-8 -*-

# A data structure is a systematic way of organizing and accessing data,
# An algorithm is a step-by-step procedure for performaing some task in
# a finite amount of time. These concepts are central to computing, but
# to be able to classify some data structures and algorithms as "good",
# we must have precise ways of nanlyzing them.

# The primary analysis tool we will use in this book involes characterizing
# the running times of algorithms and data structure operations, with space
# usage also being of interest.

# Experimental Studies

# If an algorithm has been implemented, we study its running time by
# executing it on various test inputs and recording the time spent
# during each execution.

# Because many processes share use of a computer's central processing unit
# (or CPU), the elasped time will depend on what other processes are
# running on the computer when the test is performed.

# Python includes a more advanced module, name timeit, to help
# automate such evaluations with repetition to account for such
# variance among trials.


from time import time
from timeit import timeit


def algorithm():
    return sum({k for k in range(100)})


def analysis_algorithm1(n):
    start_time = time()      # record the starting time

    for _ in range(n):
        algorithm()

    end_time = time()        # record the ending time
    elapsed = end_time - start_time
    print(elapsed)


def analysis_algorithm2(n):
    elapsed = timeit(
        stmt='algorithm()',
        setup='from __main__ import algorithm',
        number=n
    )
    print(elapsed)

# Challenges of Experimential Analysis

# While experimental studies of running times are valuable, especially when
# finetuning production-quality mode, there are three major limitations to
# their use for algorithm analysis:

    # Experimental running times of two algorithms are difficult to directly
    # compare unless the experiments are performed in the same hardware and
    # software environemnts.

    # Experiments can be done only on a limited set of test inputs; hence,
    # they leave out the running times of inputs not included in the experiment
    # (and these inputs may be important).

    # An algorithm must be fully implemented in order to execute it to study
    # its running time experimentally.


if __name__ == '__main__':
    analysis_algorithm1(100000)
    analysis_algorithm2(100000)

"""
$ py3 algorithm analysis.py
0.5058159828186035
0.5283690920041408
"""
