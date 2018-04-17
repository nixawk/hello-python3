#!/usr/bin/python
# -*- coding: utf-8 -*-


# Problem

# You need to unpack N elements from an iterable, but the iterable may be
# longer than N elements, causing a "too many values to unpack" exception.

# Solution

# Python "start expressions" can be used to address this problem. 

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record

print(phone_numbers)


# The starred variable can also be the first one in the list.

# Discussion

# Exteneded iterable unpacking is tailor-made for unpacking iterables
# of unknown or arbitrary length. Oftentimes, these iterables have
# some known component or pattern in their construction, and star
# unpacking lets the developer leverage those patterns easily instead
# of performing acrobatics to get at the relevant elements in the
# iterable.

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')

print(uname, homedir, sh)

# Sometimes you might want to unpack values and throw them away. You
# can't just specify a bare * when unpacking, but you could use a
# common throwaway variable name, such as _ or ign (ignored).
# For example

record = ('ACME', 50, 123.45, (16, 4, 2018))
name, *_, (*_, year) = record

print(name, year)

# Be aware that recursion really isn't a strong Python feature due
# to the inherent recursion limit.