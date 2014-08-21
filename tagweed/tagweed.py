#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function
import os
import sys
import pprint
import collections
import difflib

try:
    from ConfigParser import SafeConfigParser
except ImportError:
    from configparser import SafeConfigParser
import argparse

from future.utils import viewkeys
from requests.auth import HTTPBasicAuth
import requests


def parse_args_and_cfg():
    '''
    Parse command line arguments and config file
    and combine into one data structure
    '''
    args = parse_command_line_args()
    cfgs = process_config_file(args['config'], args['source'])

    for k in viewkeys(cfgs):
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

    lst_vld_actions = ['FINDSIMILAR', 'FINDPLURALS']
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


def gettagsexternal(args):
    '''
    Get tags from the external service
    '''
    r = requests.get(args['taggeturl'], auth=HTTPBasicAuth(args['userid'], args['password']))
    r.raise_for_status()
    dtags = r.json()
    return dtags


def gettagslocal(args):
    '''
    Get tags from the local repository
    '''
    raise NotImplementedError("Local tags are not yet supported")


def gettags(args):
    '''
    Return a dictionary keyed on tag names and with a
    value corresponding to the number of associated elements
    '''

    if args['source'] == "LOCAL":
        dtags = gettagslocal(args)
    else:
        dtags = gettagsexternal(args)

    return dtags


def find_similar_tags(dtags, simquotient):
    '''
    Returns a dictionary, the keys of which are a tag
    and the value of which is a string of other tags
    which are distinctly similar to the key
    '''
    dsims = collections.defaultdict(list)
    print(type(dtags))
    print("")
    ltags = dtags.keys()

    for t in ltags:
        # Get similar match
        matches = difflib.get_close_matches(t, ltags, 3, simquotient)
        # Remove the tag itself from the similarities
        if t in matches:
            matches.remove(t)
        if len(matches) > 0:
            dsims[t] = matches

    return dsims


def find_plural_tags(dtags):
    '''
    Find tags which differ only because one is a plural of
    the other.

    Note that only "common" plurals are looked for as dealing
    with the irregular cases would generate too many false positives

    Returns a dictionary keyed by a, potentially, unwanted plural the
    value of which is the, presumably, wanted singular
    '''
    dplurals = {}
    dsingular = []
    #for k in dtags.iterkeys():
    for k in viewkeys(dtags):
        if k not in dsingular:
            dsingular.append(k)
            plural_type_a = "%ss" % (k)
            plural_type_b = "%ses" % (k)
            if plural_type_a in dtags:
                dplurals[plural_type_a] = k
            if plural_type_b in dtags:
                dplurals[plural_type_b] = k

    return dplurals


def innermain_findsimilar(dtags):
    '''
    Handle FINDSIMILAR processing
    '''
    dsims = find_similar_tags(dtags, 0.8)
    print(len(dsims))
    print(len(dtags))
    pprint.pprint(dsims)

def innermain_findplurals(dtags):
    '''
    Handle FINDPLURALS processing
    '''
    dplurals = find_plural_tags(dtags)
    pprint.pprint(dplurals)

def innermain(args):
    '''Processing for the tagweed CLI after config data has been gathered'''
    dtags = gettags(args)
    if args['action'] == 'FINDSIMILAR':
        innermain_findsimilar(dtags)
    elif args['action'] == 'FINDPLURALS':
        innermain_findplurals(dtags)
    else:
        raise NotImplementedError("An action of : %s is not a valid choice")


def main():
    '''Main entry point for the tagweed CLI.'''
    #args = configuration.parse_args_and_cfg()
    args = parse_args_and_cfg()
    print(args)
    tagsdict = innermain(args)
    print(tagsdict)


if __name__ == '__main__':
    main()
