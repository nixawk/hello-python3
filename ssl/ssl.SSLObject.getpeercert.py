#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
SSLSocket.getpeercert(binary_form=False)

If there is no certificate for the peer on the other end of the connection,
return None. If the SSL handshake hasn’t been done yet, raise ValueError.


If the binary_form parameter is False, and a certificate was received from
the peer, this method returns a dict instance. If the certificate was not
validated, the dict is empty. If the certificate was validated, it returns
a dict with several keys, amongst them subject (the principal for which the
certificate was issued) and issuer (the principal issuing the certificate).
If a certificate contains an instance of the Subject Alternative Name extension
(see RFC 3280), there will also be a subjectAltName key in the dictionary.
"""

import ssl
import socket
import pprint


def ssl_SSLObject_getpeercert():
    context = ssl.create_default_context()
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    context.load_verify_locations('/etc/ssl/cert.pem')
    # ssl.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed

    conn = context.wrap_socket(
        socket.create_connection(("www.python.org", 443)),
        server_hostname="www.python.org"
    )
    cert = conn.getpeercert()
    pprint.pprint(cert)


if __name__ == '__main__':
    ssl_SSLObject_getpeercert()


"""
$ python3 ssl.SSLObject.getpeercert.py
{'OCSP': ('http://ocsp.digicert.com',),
 'caIssuers': ('http://cacerts.digicert.com/DigiCertSHA2ExtendedValidationServerCA.crt',),
 'crlDistributionPoints': ('http://crl3.digicert.com/sha2-ev-server-g2.crl',
                           'http://crl4.digicert.com/sha2-ev-server-g2.crl'),
 'issuer': ((('countryName', 'US'),),
            (('organizationName', 'DigiCert Inc'),),
            (('organizationalUnitName', 'www.digicert.com'),),
            (('commonName', 'DigiCert SHA2 Extended Validation Server CA'),)),
 'notAfter': 'Sep 27 12:00:00 2018 GMT',
 'notBefore': 'Mar 28 00:00:00 2018 GMT',
 'serialNumber': '0C4A84238E7344559BB84D1E0F318883',
 'subject': ((('businessCategory', 'Private Organization'),),
             (('jurisdictionCountryName', 'US'),),
             (('jurisdictionStateOrProvinceName', 'Delaware'),),
             (('serialNumber', '3359300'),),
             (('countryName', 'US'),),
             (('stateOrProvinceName', 'New Hampshire'),),
             (('localityName', 'Wolfeboro'),),
             (('organizationName', 'Python Software Foundation'),),
             (('commonName', 'www.python.org'),)),
 'subjectAltName': (('DNS', 'www.python.org'),
                    ('DNS', 'docs.python.org'),
                    ('DNS', 'bugs.python.org'),
                    ('DNS', 'wiki.python.org'),
                    ('DNS', 'hg.python.org'),
                    ('DNS', 'mail.python.org'),
                    ('DNS', 'pypi.python.org'),
                    ('DNS', 'packaging.python.org'),
                    ('DNS', 'login.python.org'),
                    ('DNS', 'discuss.python.org'),
                    ('DNS', 'us.pycon.org'),
                    ('DNS', 'pypi.io'),
                    ('DNS', 'docs.pypi.io'),
                    ('DNS', 'pypi.org'),
                    ('DNS', 'docs.pypi.org'),
                    ('DNS', 'donate.pypi.org'),
                    ('DNS', 'devguide.python.org'),
                    ('DNS', 'www.bugs.python.org'),
                    ('DNS', 'python.org')),
 'version': 3}
"""

# refernce
# https://docs.python.org/3/library/ssl.html#ssl.SSLSocket.getpeercert
