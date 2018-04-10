#!/usr/bin/python
# -*- coding: utf-8 -*-

# Indentation

# Use 4 spaces per indentation level.

# Continuation lines should align wrapped elements either vertically using
# Python's implicit line joining inside parentheses, brackets, and braces,
# or using a hanging indent. When using a hanging indent the following
# should be considered; there should be no arguments on the first line
# and further indentation should be used to clearly distinguish itself
# as a continutation line.

# More indentation included to distinguish this from the rest.
def long_function_name(
        var_one, var_two,
        var_three, var_four):
    '''demo for Code layout Indentation'''
    # code here
    return (var_one, var_two, var_three, var_four)

# Aligned with opening delimiter.
long_function_name(11111111111, 2222222222,
                   33333333333, 4444444444)


# When the conditional part of an if-statement is long enough to require
# that it be written across multiple lines, it's worth nothing that the
# combination of a two character keyword, plus a single space, plus an
# opening parenthesis creates a natural 4-spaces indent for the subsequent
# lines of the multiline conditional. This can produce a visual conflict
# with the indented suite of code nested inside the if-statement, which
# would also naturally be indented to 4 spaces.

# Add a comment, which will provide some distinction in editors
# support syntax highlighting
if (11111111111 < 2222222222 and
    33333333333 < 4444444444):  # Pylinter warning here.
    # Since both conditions are true, we can forbnicate.
    print('demo indentation')

# Add some extra indentation on the conditional continuation line.
if (11111111111 < 2222222222 and
        33333333333 < 4444444444):
    # Since both conditions are true, we can forbnicate.
    print('demo indentation')

# The closing brace/bracket/parenthesis on multiline constructs either
# line up under the first non-whitespace character of the last line of list

# Tabs or Spaces ?

# Tabs should be used solely to remain consistent with code that is already
# indented with tabs.

# Python 3 disallows mixing the use of tabs and spaces for indetation.

# Python 2 code indented with a mixture of tabs and spaces should be converted
# to using spaces exclusively.

# When invoking the Python 2 command line interpreter with the -t option, it
# issues warnings about code that illegally mixes tabs and spaces. When using
# -tt these warnings become errors. These options are highly recommended.

# https://www.python.org/dev/peps/pep-0008/#indentation
