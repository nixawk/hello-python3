#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
webbrowser.open(url, new=0, autoraise=True)

Display url using the default browser.

If new is 0, the url is opened in the same browser window if possible.
If new is 1, a new browser window is opened if possible.
If new is 2, a new browser page (“tab”) is opened if possible.

If autoraise is True, the window is raised if possible
(note that under many window managers this will occur
regardless of the setting of this variable).


"""

# python -m webbrowser -t "http://www.python.org"

import webbrowser


def webbrowser_open():
    status = webbrowser.open("https://www.google.com/")

    print(status)


if __name__ == '__main__':
    webbrowser_open()


# reference
# https://docs.python.org/3/library/webbrowser.html