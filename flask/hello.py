#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return "hello, world"


if __name__ == '__main__':
    app.run(debug=True)

    # FLASK_APP=hello.py flask run
    # export FLASK_APP=hello.py
    # export FLASK_ENV=development
    # flask run --host=0.0.0.0

# reference
# http://flask.pocoo.org/
# http://flask.pocoo.org/docs/1.0/quickstart/