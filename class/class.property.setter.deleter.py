#!/usr/bin/python
# -*- coding: utf-8 -*-

class Person(object):

	def __init__(self, first_name):
		super(Person, self).__init__()
		self.first_name = first_name    # Not an error (self._first_name)

	# Getter function
	@property
	def first_name(self):
		return self._first_name

	# Setter function
	@first_name.setter
	def first_name(self, value):
		if not isinstance(value, str): raise TypeError('Expected a string')
		self._first_name = value

	# Deleter function (optional)
	@first_name.deleter
	def first_name(self):
		raise AttributeError("Can't delete attribute")


if __name__ == '__main__':
	person = Person('Python')
	print(person.first_name)

	person.first_name = 'Python3'
	print(person.first_name)

	del person.first_name