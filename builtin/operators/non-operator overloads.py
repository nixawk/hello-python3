#!/usr/bin/python
# -*- coding: utf-8 -*-

# Non-Operator Overloads

# In addition to traditional operator overloading, Python relies on specially
# named methods to control the behavior of various other functionality, when
# applied to user-defined classes.

# a + b              ---- a.__add__(b)
# a - b              ---- a.__sub__(b)
# a * b              ---- a.__mul__(b)
# a / b              ---- a.__truediv__(b)
# a // b             ---- a.__floordiv__(b)
# a % b              ---- a.__mod__(b)
# a ** b             ---- a.__pow__(b)
# a << b             ---- a.__lshift__(b)
# a >> b             ---- a.__rshift__(b)
# a & b              ---- a.__and__(b)
# a ^ b              ---- a.__xor__(b)
# a | b              ---- a.__or__(b)
# a += b             ---- x.__iadd__(b)
# a -= b             ---- x.__isub__(b)
# a *= b             ---- x.__imul__(b)
# +a                 ---- a.__pos__()
# -a                 ---- a.__neg__()
# ~a                 ---- a.__invert__()
# abc(a)             ---- a.__abs__()
# a < b              ---- a.__lt__(b)
# a <= b             ---- a.__le__(b)
# a > b              ---- a.__gt__(b)
# a >= b             ---- a.__ge__(b)
# a == b             ---- a.__eq__(b)
# a != b             ---- a.__ne__(b)
# v in a             ---- a.__contains__(v)
# a[k]               ---- a.__getitem__(k)
# a[k] = v           ---- a.__setitem__(k, v)
# del a[k]           ---- a.__delitem__(k)
# a(arg1, arg2, ...) ---- a.__call__(arg1, arg2)
# len(a)             ---- a.__len__()
# hash(a)            ---- a.__hash__()
# iter(a)            ---- a.__iter_()
# next(a)            ---- a.__next__()
# bool(a)            ---- a.__bool__()
# float(a)           ---- a.__float__()
# int(a)             ---- a.__int__()
# repr(a)            ---- a.__repr__()
# reversed(a)        ---- a.__reversed__()
# str(a)             ---- a.__str__()


class Operator_Overload:

    def __str__(self):
        return "demo for operator overloading"


oo = Operator_Overload()
print(str(oo))
