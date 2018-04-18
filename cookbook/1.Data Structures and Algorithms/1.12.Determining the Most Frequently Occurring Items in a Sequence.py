#!/usr/bin/python
# -*- coding: utf-8 -*-

# Problem

# You have a sequence of items, and you'd like to determine the most frequently
# occurring items in the sequence.

# Solution

# The collections.Counter class is designed for just such a problem. It even
# comes with a handy most_common() method that will give you the answer.

# To illustrate, let's say you have a list of words and you want to find
# out which words occur most often.

from collections import Counter


words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

# Discussion

# As input, Counter objects can be fed any sequence of hashable input items.
# Under the covers, a Counter is a dictionary that maps the items to the
# number of occurrences.

# Needless to say, Counter objects are a tremendously useful tool for
# almost any kind of problem where you need to tabulate and count data.
# You should prefer this over manually solutions involving dictionaries.


# https://docs.python.org/3/library/collections.html
