#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''tagweed

Usage:
  tagweed ship new <name>...
  tagweed ship <name> move <x> <y> [--speed=<kn>]
  tagweed ship shoot <x> <y>
  tagweed mine (set|remove) <x> <y> [--moored|--drifting]
  tagweed -h | --help
  tagweed --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
'''
from __future__ import unicode_literals, print_function
from optparse import OptionParser
import os
import ConfigParser


def uidpwd(service_name, path_to_cfg):
    '''
    Read config file to get uid and pwd
    '''
    cp = ConfigParser.ConfigParser()
    cp.read(path_to_cfg)
    uid = cp.get(service_name, "uid")
    pwd = cp.get(service_name, "pwd")

    return uid, pwd


def parse_args():
    '''
    Parses command line arguments using OptionParser.
    Applies validation rules to arguments and then, if OK
    returns them in a 'dictionary like' object ``options``

    '''
    desc = "%prog is used to highlight tags which might be changed and so \n" + \
           "improve the usefulness of the set of tags.\n" + \
           "\n\n" + \
           "Command line options specify the location of a config file and the" + \
           "location of the tags."

    usage_inner = "Usage: %s [options]"
    usage = usage_inner % "%prog"

    parser = OptionParser(description=desc, usage=usage)
    parser.add_option("-c", "--config", action="store",  dest="cfg",
                      metavar="CONFIG", help="Full path to config data")
    parser.add_option("-t", "--tagsource", action="store", dest="tagsource",
                      metavar="TAGSOURCE", help="Name of TAGSOURCE (currently only PINBOARD is supported")
    parser.add_option("-v", "--verbose", action="store_true",
                      dest="verbose", help="Show progress messages")

    (options, args) = parser.parse_args()  # pylint: disable=W0612

    if (options.cfg is None) or (options.tagsource is None):
        parser.print_help()
        exit(-1)
    elif not os.path.exists(options.cfg):
        parser.error('config location does not exist')

    return options


def notmain():
    '''
    Only for the purpose of testing the testing
    '''
    print("hello")


def main():
    '''Main entry point for the tagweed CLI.'''
    print("hello")
    print("1" * 40)
    print("About torun parse_args")
    print("2" * 40)
    args = parse_args()
    print(args)

if __name__ == '__main__':
    notmain()
    main()
