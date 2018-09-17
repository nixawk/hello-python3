#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import functools


def send_whois_query(domain, whois_server, whois_server_port=43):
    """WHOIS is a TCP-based transaction-oriented query/response protocol
    that is widely used to provide information services to Internet
    users.  While originally used to provide "white pages" services and
    information about registered domain names, current deployments cover
    a much broader range of information services.  The protocol delivers
    its content in a human-readable format.  This document updates the
    specification of the WHOIS protocol, thereby obsoleting RFC 954
    """

    client = socket.create_connection((whois_server, whois_server_port))
    client.send(b"%s\r\n" % domain.encode())
    answer = []

    while True:
        _ = client.recv(1024)
        if not _:
            break
        answer.append(_)

    return "".join(list(map(lambda x: x.decode(), answer)))


if __name__ == '__main__':
    answer = send_whois_query('google.com', 'whois.verisign-grs.com')
    print(answer)


# reference
# https://tools.ietf.org/html/rfc3912
# http://www.iana.org/domains/root/db
# https://www.iana.org/domains/root/db/com.html
# https://ian.ucsd.edu/papers/imc15-whois.pdf