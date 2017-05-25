#!/usr/bin/python
# -*- coding: utf-8 -*-

import abc
import io


class ABCWithConcreteImplementation(abc.ABC):

    @abc.abstractmethod
    def retrieve_values(self, input):
        print('base class reading data')
        return input.read()


class ConcreteOverride(ABCWithConcreteImplementation):

    def retrieve_values(self, input):
        base_data = super(ConcreteOverride, self).retrieve_values(input)
        print('subclass sorting data')
        response = sorted(base_data.splitlines())
        return response


if __name__ == '__main__':
    input = io.StringIO("""line one
line two
line three
"""
    )

    reader = ConcreteOverride()
    print(reader.retrieve_values(input))


"""
$ python abc_concrete_method.py
base class reading data
subclass sorting data
['line one', 'line three', 'line two']
"""

"""
Since ABCWithConcreteImplementation() is an abstract base class, it is not possible to instantiate it to use it directly.
Subclasses must provide an override for retrieve_values(), and in this case the concrete class sorts the data before returning it.
"""