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
import os
import sys
import ConfigParser
import argparse


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

    lst_vld_actions = ['FINDSIMILAR']
    lst_vld_sources = ['PINBOARD', 'LOCAL']

    action_help = 'the process to be executed. Valid values : %s' % "|".join(lst_vld_actions)
    source_help = 'either the name of the service hosting the tags or "LOCAL" where tags are in a local file. Valid values : %s' % "|".join(lst_vld_sources)

    parser = argparse.ArgumentParser(description='Provides assistance in cleaning sets of tags.')
    parser.add_argument('-c', '--config', required=True, help='path to the config file')
    parser.add_argument('-a', '--action', required=True,  help=action_help)
    parser.add_argument('-s', '--source', required=False,  help=source_help)

    args = vars(parser.parse_args())

    if args['action'] not in lst_vld_actions:
        sys.exit("Only %s are valid actions" % "|".join(lst_vld_actions))

    if args['source'] not in lst_vld_sources:
        sys.exit("Only %s are valid sources" % "|".join(lst_vld_sources))

    if not os.path.isfile(args['config']):
        sys.exit("%s is not a file" % args['config'])

    return args


def main():
    '''Main entry point for the tagweed CLI.'''
    args = parse_args()
    innermain(args)


def innermain(args):
    '''Main processing for the tagweed CLI.'''

if __name__ == '__main__':
    main()
