#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# string: (default) accepts any text without a slash
# int: accepts positive integers
# float: accepts positive floating point values
# path: like string but also accepts slashes
# uuid: accepts UUID strings

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return (
        "/user/YourUser (required, a str)<br />"
        "/age/YourAge (required, a int)"
    )


@app.route('/user/<string:username>')
def get_username(username):
    return "hello, %s" % username


@app.route('/age/<int:age>')
def get_age(age):
    return "age is %d" % age


if __name__ == '__main__':
    app.run()


# reference
# http://flask.pocoo.org/docs/1.0/quickstart/#variable-rules