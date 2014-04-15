#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals, print_function

from requests.auth import HTTPBasicAuth
import requests

import configuration

def main():
    '''Main entry point for the tagweed CLI.'''
    args = configuration.parse_args_and_cfg()
    tagsdict = innermain(args)


def innermain(args):
    '''Main processing for the tagweed CLI.'''
    print(args)
    r = requests.get(args['taggeturl'], auth=HTTPBasicAuth(args['userid'], args['password']))
    r.raise_for_status()
    dtags = r.json()
    return dtags

if __name__ == '__main__':
    main()
