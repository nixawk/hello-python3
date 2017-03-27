#!/usr/bin/python
# -*- coding: utf-8 -*-

from mysql.connector import (connection)


cnx = connection.MySQLConnection(
    user='root', password='password',
    host='127.0.0.1',
    database='mysql'
)
cnx.close()

"""
Both methods, using the connect() constructor, or the class directly, are valid
and functionally equal, but using connector() is preferred and is used in most
examples in this manual.
"""
