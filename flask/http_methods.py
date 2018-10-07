#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import (
    Flask,
    request
)


app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "POST /login"
    else:
        return "GET /login"


if __name__ == '__main__':
    app.run()

# reference
# http://flask.pocoo.org/docs/1.0/quickstart/#http-methods
