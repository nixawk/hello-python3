#!/usr/bin/python
# -*- coding: utf-8 -*-

import mysql.connector


cnx = mysql.connector.connect(
    user='root', password='password',
    host='127.0.0.1',
    database='mysql'
)
cnx.close()
