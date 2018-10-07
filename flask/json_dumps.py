#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return json.dumps({'hello': 'world'})


if __name__ == '__main__':
    app.run()