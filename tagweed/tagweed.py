#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

from requests.auth import HTTPBasicAuth
import requests

import configuration

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
    if args['source'] == "LOCAL":
        dtags = gettagslocal(args)
    else:
        dtags = gettagsexternal(args)

def innermain(args):
    '''Processing for the tagweed CLI after config data has been gathered'''
    dtags = gettags(args)

def main():
    '''Main entry point for the tagweed CLI.'''
    args = configuration.parse_args_and_cfg()
    print(args)
    tagsdict = innermain(args)


if __name__ == '__main__':
    main()
