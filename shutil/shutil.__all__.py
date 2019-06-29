#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import shutil


if __name__ == '__main__':
    for name in shutil.__all__:
        print(f"shutil.{name}")

"""
$ py3 shutil.__all__.py
shutil.copyfileobj
shutil.copyfile
shutil.copymode
shutil.copystat
shutil.copy
shutil.copy2
shutil.copytree
shutil.move
shutil.rmtree
shutil.Error
shutil.SpecialFileError
shutil.ExecError
shutil.make_archive
shutil.get_archive_formats
shutil.register_archive_format
shutil.unregister_archive_format
shutil.get_unpack_formats
shutil.register_unpack_format
shutil.unregister_unpack_format
shutil.unpack_archive
shutil.ignore_patterns
shutil.chown
shutil.which
shutil.get_terminal_size
shutil.SameFileError
shutil.disk_usage
"""
