"""The module is for redis cache."""
# -*- coding: utf-8 -*-

import os
import urllib
import requests
import redis


CACHE = redis.StrictRedis(host='localhost', port=6379, db=0)


def download(image_url):
    """download a image, and cache it in redis.
    """
    name = os.path.basename(urllib.parse.urlparse(image_url).path)

    image = CACHE.get(name)
    if image is None:
        print('Cache miss', flush=True)
        response = requests.get(image_url)
        CACHE.set(name, response.content)


if __name__ == '__main__':
    URL = 'https://redis.io/images/redis-white.png'
    download(URL)


## references
# https://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python