#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
webbrowser.open_new(url)

Open url in a new window of the default browser, if possible,
otherwise, open url in the only browser window.


webbrowser.open_new_tab(url)

Open url in a new page (“tab”) of the default browser, if possible,
otherwise equivalent to open_new().

"""

# python -m webbrowser -t "http://www.python.org"

import webbrowser


def webbrowser_open_new():
    status = webbrowser.open_new("https://www.google.com/")

    print(status)


if __name__ == '__main__':
    webbrowser_open_new()


# reference
# https://docs.python.org/3/library/webbrowser.html