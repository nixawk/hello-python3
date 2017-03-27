#!/usr/bin/python
# -*- coding: utf-8 -*-

import mysql.connector


config = {
    'user': 'root',
    'password': 'password',
    'host': '127.0.0.1',
    'database': 'mysql',
    'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)
cnx.close()

# If you have lots of connection arguments, it's best to keep them in a
# dictionary and use the ** operator.
