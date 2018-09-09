#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import ssl


def client_socket():
    host = '127.0.0.1'
    port = 8443
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.load_verify_locations('server.crt')

    with socket.create_connection((host, port)) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            print(ssock.version())
            print(ssock.recv(512).decode())


if __name__ == '__main__':
    client_socket()


# openssl genrsa -des3 -out server.key 2048 
# openssl rsa -in server.key -out server.key
# openssl req -new -x509 -key server.key -out ca.crt -days 3650 
# openssl x509 -req -days 3650 -in server.csr -CA ca.crt -CAkey server.key -CAcreateserial -out server.crt
# cat server.key server.crt > server.pem

# reference
# https://docs.python.org/3/library/ssl.html#socket-creation
# https://stackoverflow.com/questions/991758/how-to-get-pem-file-from-key-and-crt-files
