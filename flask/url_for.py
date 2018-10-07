#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

# /
# /login
# /login?next=/
# /user/John%20Doe

# http://flask.pocoo.org/docs/1.0/quickstart/#url-building