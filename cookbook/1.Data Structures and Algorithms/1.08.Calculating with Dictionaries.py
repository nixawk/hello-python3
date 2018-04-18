#!/usr/bin/python
# -*- coding: utf-8 -*-

# Problem

# You want to perform various calculations on a dictionary of data.

# Solution

# Consider a dictionary that maps stock names to prices

prices = {
    'ACME': 45.32,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}


# In order to perform useful calculations on the dictionary contents,
# it is often useful to invert the keys and values of the dictionary
# using zip().

min_price = min(zip(prices.values(), prices.keys()))

max_price = max(zip(prices.values(), prices.keys()))

# When doing these calculations, be aware that zip() creates an iterator
# that can only be consumed once. For example,

    # The following code is an error

    # prices_and_names = zip(prices.values(), prices.keys())
    # print(min(prices_and_names))  # OK
    # print(max(prices_and_names))  # ValueError: max() arg is an empty sequence

# You can get the key corresponding to the min or max value if you supply
# a key function to min() and max().

    # min(prices, key=lambda k: prices[k])
    # max(prices, key=lambda k: prices[k])
