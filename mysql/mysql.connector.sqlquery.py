import mysql.connector
import logging


# $ sudo pip install mysql-connector

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


def sql_query(host, port, username, password, sql, db=None, timeout=5):
    result = None
    try:
        client = mysql.connector.connect(
            host=host, port=int(port),
            user=username, password=password,
            database=db,
            connect_timeout=timeout
        )
        cursor = client.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        client.close()
    except Exception as e:
        log.debug("Error: {} / {}".format(sql, e))
    return result


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 3306
    username = 'root'
    password = 'password'
    sql = 'select @@version;'

    result = sql_query(host, port, username, password, sql)
    print(result)


## References:
# 1. https://pypi.python.org/pypi/mysql-connector-python/
# 2. https://downloads.mysql.com/docs/connector-python-en.a4.pdf
