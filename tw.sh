#!/bin/bash
CONF=./tagweed/sample.cfg
USER=$1
PWD=$2
#
python ./tagweed/tagweed.py -c $CONF -a FINDSIMILAR -s PINBOARD  -u $USER -p $PWD 
