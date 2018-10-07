#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import (
    Flask,
    json
)


app = Flask(__name__)


@app.route('/')
def index():
    return json.dumps({'hello': 'world'})


if __name__ == '__main__':
    app.run()