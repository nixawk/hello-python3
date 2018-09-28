#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ftplib import FTP
from ftplib import error_perm
from pprint import pprint
import logging


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__file__)


class FtpDownloader(object):
    def __init__(self, *args, **kwargs):
        super(FtpDownloader, self).__init__()

        self._args = args
        self._kwargs = kwargs

        self.host = self._kwargs.get('host')
        self.user = self._kwargs.get('user')
        self.passwd = self._kwargs.get('passwd')
        self.client = None
        self.md5tbl = {}
        self._md5 = None

    def __enter__(self):
        self.client = FTP(host=self.host)
        self.client.login(user=self.user, passwd=self.passwd)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.client.close()
        self.client = None

    def retrbinary_retr_callback(self, s):
        rawdata = s.decode()
        md5, filename = rawdata.split(maxsplit=1)
        # print(md5, filename.strip())
        self._md5 = md5

    def read_file(self, filename):
        self.client.retrbinary(
            'RETR %s' % filename,
            self.retrbinary_retr_callback
        )

    def read_md5_file(self, filename):
        if filename.endswith('MD5'):
            self.read_file(filename)

    def walk_dir(self, path='/'):
        original_dir = self.client.pwd()

        try:
            self.client.cwd(path)
        except error_perm:
            return  # ignore non-directores and ones we cannot enter

        filenames = self.client.mlsd(path)
        for filename, fileinfo in filenames:
            if fileinfo.get('type') == 'dir':
                log.debug('walk_dir: %s/%s' % (original_dir, filename))
                self.walk_dir(original_dir + filename)

            elif fileinfo.get('type') == 'file':
                fullpath = path + '/' +  filename
                log.debug('read_md5_file: %s' % fullpath)
                self.read_md5_file(filename)
                self.md5tbl[fullpath] = self._md5
                self._md5 = None

        self.client.cwd(original_dir)


if __name__ == '__main__':
    config = {
        'host': 'ftp.example.com',
        'user': 'username',
        'passwd': 'password',
    }

    with FtpDownloader(**config) as ftpdownloader:
        ftpdownloader.walk_dir('/')
        pprint(ftpdownloader.md5tbl)


# reference
# https://docs.python.org/3/library/ftplib.html#ftplib.FTP.retrbinary
# https://docs.python.org/3/library/ftplib.html#ftplib.FTP.mlsd
# https://stackoverflow.com/questions/1854572/traversing-ftp-listing
# https://stackoverflow.com/questions/111954/using-pythons-ftplib-to-get-a-directory-listing-portably
# https://erlerobotics.gitbooks.io/erle-robotics-python-gitbook-free/file_transfer_protocol_ftp/detecting_directories_and_recursive_download.html