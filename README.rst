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

    (venv3)~/dev/tagweed $ python tagweed.py -c sample.cfg -a FINDSIMILAR -s LOCAL -l sampletags.json

Pinboard.in source of tags::

    (venv3)~/dev/tagweed/tagweed $ python tagweed.py -c sample.cfg -a FINDSIMILAR -s PINBOARD  -u foo -p bar


Virtualenv Usage
-----
Originally I had a virtualenv based on Python 2.7. At the same time I had a number of problems with tox. As part of the process of fixing the tox problems I tried changing the 'native' virtualenv to a Python 3.4 one. Whether or not this was part of the solution with tox I've stuck with it so the `venv3` directory is the virtualenv used for normal usage (and the `.tox` directory contains the virtualenvs used by tox).
