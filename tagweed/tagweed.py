#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''tagweed2

Usage:
  tagweed2 ship new <name>...
  tagweed2 ship <name> move <x> <y> [--speed=<kn>]
  tagweed2 ship shoot <x> <y>
  tagweed2 mine (set|remove) <x> <y> [--moored|--drifting]
  tagweed2 -h | --help
  tagweed2 --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.
'''
from __future__ import unicode_literals, print_function
from docopt import docopt

def main():
    '''Main entry point for the tagweed2 CLI.'''
    args = docopt(__doc__, version=__version__)
    print(args)

if __name__ == '__main__':
    main()
