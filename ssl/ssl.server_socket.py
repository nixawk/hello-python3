#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ssl
import socket


def server_socket():
    host = "127.0.0.1"
    port = 8443
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain("server.crt", "server.key")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
        print("[+] listening on %s:%d...." % (host, port))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((host, port))
        sock.listen(5)
        with context.wrap_socket(sock, server_side=True) as ssock:
            conn, addr = ssock.accept()
            print(addr)
            conn.send("hello ssl\n".encode())


if __name__ == '__main__':
    server_socket()


# openssl genrsa -des3 -out server.key 2048 
# openssl rsa -in server.key -out server.key
# openssl req -new -x509 -key server.key -out ca.crt -days 3650 
# openssl x509 -req -days 3650 -in server.csr -CA ca.crt -CAkey server.key -CAcreateserial -out server.crt
# cat server.key server.crt > server.pem


# reference
# https://docs.python.org/3/library/ssl.html#socket-creation
# https://stackoverflow.com/questions/6380057/python-binding-socket-address-already-in-use
