#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import os
import sys
from ConfigParser import SafeConfigParser
import argparse

def parse_args_and_cfg():
    '''
    Parse command line arguments and config file
    and combine into one data structure
    '''
    args = parse_command_line_args()
    cfgs = process_config_file(args['config'], args['source'])

    for k in cfgs.iterkeys():
        if k in args:
            sys.exit("The config key : %s also appears as a \
                    command line argument keyword. Fatal error" % k)
        else:
            args[k] = cfgs[k]

    return args


def process_config_file(path_to_cfg_file, source):
    '''
    Extract relevant values from config file
    '''
    if source == "LOCAL":
        d = {}
    else:
        parser = SafeConfigParser()
        parser.read(path_to_cfg_file)
        tag_get_url = parser.get(source, 'taggeturl')
        d = {'taggeturl': tag_get_url}

    return d


def parse_command_line_args():
    '''
    Parse command line args and do some rudimentary validation
    '''

    lst_vld_actions = ['FINDSIMILAR','FINDPLURALS']
    lst_vld_sources = ['PINBOARD', 'LOCAL']

    action_help = 'the process to be executed. Valid values : %s' % "|".join(lst_vld_actions)
    source_help = 'either the name of the service hosting the tags or "LOCAL" where tags are in a local file. Valid values : %s' % "|".join(lst_vld_sources)

    parser = argparse.ArgumentParser(description='Provides assistance in cleaning sets of tags.')
    parser.add_argument('-c', '--config', required=True, help='Path to the config file')
    parser.add_argument('-a', '--action', required=True, help=action_help)
    parser.add_argument('-s', '--source', required=True, help=source_help)
    parser.add_argument('-u', '--userid', required=False, help="Userid to access tag cloud")
    parser.add_argument('-p', '--password', required=False, help="Password to access tag cloud")
    parser.add_argument('-l', '--localfile', required=False, help="Path to local JSON containing tags")

    args = vars(parser.parse_args())

    if args['action'] not in lst_vld_actions:
        sys.exit("Only %s are valid actions" % "|".join(lst_vld_actions))

    if args['source'] not in lst_vld_sources:
        sys.exit("Only %s are valid sources" % "|".join(lst_vld_sources))

    if not os.path.isfile(args['config']):
        sys.exit("The 'config' file path %s is not a file" % args['config'])

    if args["source"] == "LOCAL":
        if args["localfile"]:
            if not os.path.isfile(args['localfile']):
                sys.exit("The 'localfile' file path %s is not a file" % args['localfile'])
        else:
            sys.exit("For source : %s the localfile must be supplied" % args['source'])
    else:
        if args["userid"] is None:
            sys.exit("For source : %s the userid must be supplied" % args['source'])
        elif args["password"] is None:
            sys.exit("For source : %s the password must be supplied" % args['source'])

    return args
