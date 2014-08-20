===============================
tagweed
===============================

.. image:: https://badge.fury.io/py/tagweed.png
    :target: http://badge.fury.io/py/tagweed

.. image:: https://travis-ci.org/shearichard/tagweed.png?branch=master
        :target: https://travis-ci.org/shearichard/tagweed

.. image:: https://pypip.in/d/tagweed/badge.png
        :target: https://crate.io/packages/tagweed?version=latest


tagweed provides help in cleaning up tag clouds such as those seen in pinboard.io, delicious.com, etc

* Free software: BSD license
* Documentation: http://tagweed.rtfd.org.

Features
--------

* TODO..


Usage
-----
Examples of usage for easy reference:

Local source of tags::

    (venv)~/dev/tagweed $ python tagweed.py -c sample.cfg -a FINDSIMILAR -s LOCAL -l sampletags.json

Pinboard.in source of tags::

    (venv)~/dev/tagweed/tagweed $ python tagweed.py -c sample.cfg -a FINDSIMILAR -s PINBOARD  -u foo -p bar
