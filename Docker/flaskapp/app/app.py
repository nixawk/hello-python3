#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, Docker"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
