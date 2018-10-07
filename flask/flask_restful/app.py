#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip install flask-restful

from flask import Flask
from flask_restful import (
    Resource,
    Api
)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


app = Flask(__name__)
api = Api(app)
api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run()

# reference
# https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api
# https://github.com/pallets/flask