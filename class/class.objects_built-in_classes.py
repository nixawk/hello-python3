#!/usr/bin/python
# -*- coding: utf-8 -*-

# Take particular note of which classes are mutable and which are immutable.
# A class is immutable if each object of that class has a fixed value upon
# instantiation that cannot subsequently be changed. For example, the float
# class is immutable. Once an instance has been created, its value cannot
# be changed (although an identifier referencing that object can be reassigned
# to a different value.)


#   Class      Description                            Immutable
#   ---------- -------------------------------------- ---------
#   bool       Boolean vaue.                          +
#   int        integer (arbitrary magnitude).         +
#   float      floating-point number                  +
#   list       mutable sequence of objects            
#   tuple      immutable sequence of objects          +
#   str        character string                       +
#   set        unordered set of distinct objects.     
#   frozenset  immutable from of set class            +
#   dict       associative mapping (aka dictionary)

CLASS_BOOL = True
print('CLASS_BOOL', id(CLASS_BOOL))

CLASS_BOOL = False
print('CLASS_BOOL', id(CLASS_BOOL))

CLASS_INT = 1
print('CLASS_INT', id(CLASS_INT))

CLASS_INT = 2
print('CLASS_INT', id(CLASS_INT))


CLASS_LIST = [1, 2, 3]
print('CLASS_LIST', id(CLASS_LIST))

CLASS_LIST[0] = 2
print('CLASS_LIST', id(CLASS_LIST))


"""
$ py3 class.objects_built-in_classes.py
CLASS_BOOL 4304933248
CLASS_BOOL 4304933216
CLASS_INT 4305324416
CLASS_INT 4305324448
CLASS_LIST 4355167752
CLASS_LIST 4355167752
"""
