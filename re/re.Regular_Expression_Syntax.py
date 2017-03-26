#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Regular Expression Syntax

'.'
    (Dot.) In the default mode, this matches any character except a newline.
    If the re.DOTALL flag has been specified, this matches any character
    including a newline.

'^'
    (Caret.) Matches the start of the string, and in re.MULTILINE mode also
    matches immediately after each line.

'$'
    Matches the end of the string or just before the newline at the end of the
    string, and in re.MULTILINE mode also matches before a newline. foo matches
    both 'foo' and 'foobar', while the regular expression foo$ matches only
    'foo'. More interestingly, searching for foo.$ in 'foo1\nfoo2\n' matches
    'foo2' normally, but 'foo1' in re.MULTILINE mode; searching for a single $
    in 'foo\n' will find two (empty) matches: one just before the newline, and
    at the end of the string.

'*'
    Causes the resulting RE to match 0 or more repetitions of the preceding RE,
    as many repetitions as are possible. ab* will match 'a', 'ab', or 'a'
    followed by any number of 'b's.

'+'
    Causes the resulting RE to match 1 or more repetitions of the preceding RE.
    ab+ will match 'a' followed by any non-zero number of 'b's; it will not
    match just 'a'.

'?'
    Causes the resulting RE to match 0 or 1 repetitions of the preceding RE.ab?
    will match either 'a' or 'ab'.

*?, +?, ??
    The '*', '+', and '?' qualifiers are all greedy, they match as much text as
    possible. Sometimes this behaviour isn't desired; if the RE <.*> is matched
    against <a> <b> <c>, it will match the entire string, and not just <a>.
    Adding ? after the qualifier makes it perform the match in non-greedy or
    minimal fashion; as few character as possible will be matched. Using the
    RE <.*?> will match only <a>.

{m}
    Specifies that exactly m copies of the previous RE should be matched; fewer
    matches cause the entire RE not to match. For example, a{6} will match
    exactly six 'a' characters, but not five.
"""

import re

s = 'Python\nis\na\ngood\nlanguage.'
regex = re.compile(r'Python(.)', re.DOTALL)
print(regex.search(s).groups())

regex = re.compile(r'^(.*)$', re.MULTILINE)
print(regex.search(s).groups())

s = '<a> <b> <c>'
regex = re.compile(r'<.*>')   # match: <a> <b> <c>
print(regex.findall(s))

regex = re.compile(r'<.*?>')  # match: <a>, <b>, <c>
print(regex.findall(s))
