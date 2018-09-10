#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
importlib.find_loader(name, path=None)

Find the loader for a module, optionally within the specified path.
If the module is in sys.modules, then sys.modules[name].__loader__
is returned (unless the loader would be None or is not set, in which
case ValueError is raised). Otherwise a search using sys.meta_path
is done. None is returned if no loader is found.

A dotted name does not have its parents implicitly imported as that
requires loading them and that may not be desired. To properly import
a submodule you will need to import all parent packages of the submodule
and use the correct argument to path.
"""

import importlib


def importlib_find_loader():
    mod = importlib.find_loader('mod')

    # create_module
    # exec_module
    # get_code
    # get_data
    # get_filename
    # get_source
    # is_package
    # load_module
    # name
    # path
    # path_mtime
    # path_stats
    # set_data
    # source_to_code

    print(mod.name)
    print(mod.path)


if __name__ == '__main__':
    importlib_find_loader()


# reference
# https://docs.python.org/3/library/importlib.html#importlib.find_loader
# https://docs.python.org/3/library/importlib.html#importlib.abc.Loader
