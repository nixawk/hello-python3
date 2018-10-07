#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Use the route() decorator to bind a function to a URL.

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Index Page"


@app.route('/hello')
def hello():
    return "Hello, World"


if __name__ == '__main__':
    app.run()


# reference
# http://flask.pocoo.org/docs/1.0/quickstart/#routing