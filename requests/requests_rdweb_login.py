#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Microsoft Remote Desktop Web Access
# Tested against Windows Server 2016

import re
import logging
import requests


logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__file__)

# Disable requests warnings
requests.urllib3.disable_warnings()


class RDWEB(object):

    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

        assert 'url' in self._kwargs.keys(), Exception("please RDWeb Home URL")
        self.rdweb_default_url = self._kwargs.get('url')
        self.rdweb_request_timeout = self._kwargs.get('timeout', 8)

    def login(self, username, password):
        """Try to login Microsoft Remote Desktop Web Access.
        """

        status = False
        resp_1 = requests.get(
            self.rdweb_default_url,
            verify=False,
            headers={'User-Agent': 'Mozilla/5.0'},
            timeout=self.rdweb_request_timeout
        )

        regex = re.compile(
            "<input type=\"hidden\" name=\"WorkSpaceID\" value=\"([^\"]+)\"/>"
        )
        match = regex.search(resp_1.text)

        if not match:
            log.info("[-] Failed to get WorkSpaceID")
            return status

        work_space_id, = match.groups()
        params = {
            'WorkSpaceID': work_space_id,
            'RDPCertificates': '',
            'PublicModeTimeout': 20,
            'PrivateModeTimeout': 240,
            'WorkspaceFriendlyName': '',
            'EventLogUploadAddress': '',
            'RedirectorName': '',
            'ClaimsHint': '',
            'ClaimsToken': '',
            'isUtf8': 1,
            'flags': 4,
            'DomainUserName': username,
            'UserPass': password,
            'MachineType': 'private'
        }
        resp_2 = requests.post(
            resp_1.url,
            data=params,
            verify=False,
            headers={'User-Agent': 'Mozilla/5.0'},
            timeout=self.rdweb_request_timeout
        )
        historys = resp_2.history
        if len(historys) >= 1:
            status = all([
                historys[0].status_code == 302,
                resp_2.status_code == 200,
                'Default.aspx' in resp_2.url
            ])

        log.info(f"[*] login {work_space_id} with ({username}:{password}), status: {status}")
        return status


if __name__ == '__main__':

    config = {
        'url': "https://password.example.com/RDWeb/",
        'timeout': 8
    }

    username = 'Example\\username'
    password = 'password'

    rdweb = RDWEB(**config)
    rdweb.login(username, password)


# references
# https://en.wikipedia.org/wiki/Remote_Desktop_Services
# https://www.rdsgurus.com/html5-client-for-microsoft-remote-desktop-services-2016-remote-desktop-web-client/
