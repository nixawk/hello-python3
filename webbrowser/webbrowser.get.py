#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
webbrowser.get(using=None)

Return a controller object for the browser type using.
If using is None, return a controller for a default
browser appropriate to the caller’s environment.
"""

import webbrowser


def webbrowser_get():
    # mozilla
    # firefox
    # netscape
    # galeon
    # epiphany
    # skipstone
    # kfmclient
    # konqueror
    # kfm
    # mosaic
    # opera
    # grail
    # links
    # elinks
    # lynx
    # w3m
    # windows-default
    # macosx
    # safari
    # google-chrome
    # chrome
    # chromium
    # chromium-browser
    browser = webbrowser.get(using='firefox')
    browser.open('https://www.google.com/')


if __name__ == '__main__':
    webbrowser_get()


# reference
# https://docs.python.org/3/library/webbrowser.html