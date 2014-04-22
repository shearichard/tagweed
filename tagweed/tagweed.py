#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

from requests.auth import HTTPBasicAuth
import requests
import pprint

import configuration
import collections
import difflib

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
        #Get similar match
        matches = difflib.get_close_matches(t, ltags, 3, simquotient)
        #Remove the tag itself from the similarities
        if t in matches:
            matches.remove(t)
        if len(matches) > 0:
            dsims[t] = matches

    return dsims

def innermain(args):
    '''Processing for the tagweed CLI after config data has been gathered'''
    dtags = gettags(args)
    dsims = find_similar_tags(dtags, 0.8) 
    print(len(dsims))
    print(len(dtags))


def main():
    '''Main entry point for the tagweed CLI.'''
    args = configuration.parse_args_and_cfg()
    print(args)
    tagsdict = innermain(args)


if __name__ == '__main__':
    main()
