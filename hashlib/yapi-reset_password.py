#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib


def generatePassword(password, passsalt):
    """ https://github.com/YMFE/yapi/blob/711d1d32ff6f059e6e63dfa0ce683d5bbd6958e0/server/utils/commons.js#L170
    exports.generatePassword = (password, passsalt) => {
      return sha1(password + sha1(passsalt));
    };
    """
    text = password + hashlib.sha1(passsalt.encode()).hexdigest()
    return hashlib.sha1(text.encode()).hexdigest()


if __name__ == '__main__':
    password = "password"
    passsalt = "qq0bcly5gts"

    passhash = generatePassword(password, passsalt)
    print(passhash)


# references
# https://github.com/YMFE/yapi
