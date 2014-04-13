#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_tagweed
----------------------------------

Tests for `tagweed` module.
"""

import unittest
import StringIO
import sys

from tagweed import tagweed


class TestTagweedArgHandling(unittest.TestCase):
    '''
    Inspired by http://stackoverflow.com/a/5975668/364088
    '''
    usestringio = True

    def setUp(self):
        if self.usestringio:
            self.output = StringIO.StringIO()
            self.saved_stdout = sys.stdout
            sys.stdout = self.output
        else:
            self.fsock = open('/home/rshea/tmp/out.log', 'w')
            self.saved_stdout = sys.stdout
            sys.stdout = self.fsock

    def tearDown(self):
        if self.usestringio:
            self.output.close()
        else:
            self.fsock.close()
        sys.stdout = self.saved_stdout

    def testYourScript1(self):
        tagweed.main()
        if self.usestringio:
            assert "hello" in self.output.getvalue()
        else:
            self.fsock.close()
            self.fsock = open('/home/rshea/tmp/out.log', 'r')
            self.outputseen = self.fsock.read()
            assert "hello" in self.outputseen


class TestTagweed(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        self.assertEqual(1, 1)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
