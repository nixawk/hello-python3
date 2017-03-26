#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
substitute(mapping, **kwds)

    Performs the template substitution, returning a new string. mapping is any
    dictionary-like object with keys that match the placeholders in the
    template. Alternatively, you can provide keyword arguments, where the
    keywords are the placeholders. When both mapping and kwds are given and
    there are duplicates, the placeholders from kwds take precedence.

safe_substitute(mapping, **kwds)

    Like substitute(), except that if placeholders are missing from mapping
    and kwds, instead of raising a KeyError exception, the original placeholder
    will appear in the resulting string intact. Also, unlike with substitute(),
    any other appearances of the $ will simply return $ instead of raising
    ValueError.

    While other exceptions may still occur, this method is called “safe”
    because substitutions always tries to return a usable string instead
    of raising an exception. In another sense, safe_substitute() may be
    anything other than safe, since it will silently ignore malformed
    templates containing dangling delimiters, unmatched braces, or
    placeholders that are not valid Python identifiers.
"""

from string import Template


hello_template = Template("${language} is a good choice.")
print(hello_template.substitute({'language': 'Python'}))

hello_template = Template("${language} is a good choice by $who.")
print(hello_template.safe_substitute({'language': 'Python'}))
