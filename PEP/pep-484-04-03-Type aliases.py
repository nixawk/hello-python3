#!/usr/bin/python
# -*- coding: utf-8 -*-

# Type aliases

# Type aliases are defined by simple variable assignments

# Note that we recommend capitalizing alias names, since they represent
# user-defined types, which (like user-defined classes) and typically
# spelled that way.

'''
Url = str


def retry(url: Url, retry_count: int) -> None:
    pass
'''

# Type aliases may be as complex as type hints in annotations
# anything that is acceptable as a type hint is acceptable in
# a type alias.

'''
T = TypeVar('T', int, float, complex)
Vector = Iterable(Tuple[T, T])


def inproduct(v: Vector[T]) -> T:
    return sum(x*y for x, y in v)


def dilate(v: Vector[T], scale: T) -> Vector[T]:
    return ((x * scale, y * scale) for x, y in v)
'''

# This is equivalent to

'''
from typing import TypeVar, Iterable, Tuple

T = TypeVar('T', int, float, complex)

def inproduct(v: Iterable[Tuple[T, T]]) -> T:
    return sum(x*y for x, y in v)
def dilate(v: Iterable[Tuple[T, T]], scale: T) -> Iterable[Tuple[T, T]]:
    return ((x * scale, y * scale) for x, y in v)
vec = []  # type: Iterable[Tuple[float, float]]
'''

from typing import TypeVar, Iterable, Tuple


AnyStr = TypeVar('AnyStr', str, bytes)
Vector = Iterable[Tuple[AnyStr, AnyStr]]


def concat(strlst: Vector[AnyStr], strval: AnyStr) -> AnyStr:
    return "".join(strlst) + strval


if __name__ == '__main__':
    print(concat(
        ['Hello', ','],
        'Python'
    ))

## References
# https://www.python.org/dev/peps/pep-0484/#type-aliases