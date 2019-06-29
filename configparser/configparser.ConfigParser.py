#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser


if __name__ == '__main__':
    cfg = configparser.ConfigParser()
    cfg.read('config.ini')

    print(cfg.get('log', 'debug'))
    print(cfg.get('server', 'port'))


"""
configparser.NoSectionError
configparser.DuplicateOptionError
configparser.DuplicateSectionError
configparser.NoOptionError
configparser.InterpolationError
configparser.InterpolationDepthError
configparser.InterpolationMissingOptionError
configparser.InterpolationSyntaxError
configparser.ParsingError
configparser.MissingSectionHeaderError
configparser.ConfigParser
configparser.SafeConfigParser
configparser.RawConfigParser
configparser.Interpolation
configparser.BasicInterpolation
configparser.ExtendedInterpolation
configparser.LegacyInterpolation
configparser.SectionProxy
configparser.ConverterMapping
configparser.DEFAULTSECT
configparser.MAX_INTERPOLATION_DEPTH
"""