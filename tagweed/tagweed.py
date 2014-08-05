#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

from requests.auth import HTTPBasicAuth
import requests
import pprint

from tagweed import configuration
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
    for k in dtags.iterkeys():
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
    args = configuration.parse_args_and_cfg()
    print(args)
    tagsdict = innermain(args)
    print(tagsdict)


if __name__ == '__main__':
    main()
