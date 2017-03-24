
"""
Any object can be tested for truth value, for use in an if or while condition
or as operand of the Boolean operations below. The following values are
considered false:

- None
- False
- zero of any numeric type, for example, 0, 0.0, 0j.
- any empty sequence, for example, '', (), [].
- any empty mapping, for example, {}
- instance of use-defined classes, if the class defines a __bool__()
  or __len__() method, when that method returns the integer
  zero or bool value False.
"""


class TruthValueTest(object):
    def __bool__(self):
        return True


class TruthValueTest2(object):
    def __len__(self):
        return False


v1 = TruthValueTest()
v2 = TruthValueTest2()

print(True if v1 else False)
print(True if v2 else False)
