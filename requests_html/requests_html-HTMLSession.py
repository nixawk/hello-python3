#!/usr/bin/python
# -*- coding: utf-8 -*-

from requests_html import HTMLSession


'''
In [1]: from requests_html import HTMLSession

In [2]: session = HTMLSession()

In [3]: r = session.get("https://python.org/")

In [4]: about = r.html.find("#about", first=True)

In [5]: about.text
Out[5]: 'About\nApplications\nQuotes\nGetting Started\nHelp\nPython Brochure'

'''

def test():
    s = HTMLSession()
    r = s.get("https://python.org/")

    # print(r.html.links)
    # print(r.html.absolute_links)
    # print(r.html.xpath('//a/@href'))

    pr = r.html.search('Python is a {} language')   # <class 'parse.Result'>
    print(pr[0])


if __name__ == '__main__':
    test()


# https://github.com/kennethreitz/requests-html