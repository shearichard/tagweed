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


class TestTagweed(unittest.TestCase):

    def setUp(self):
        pass

    def test_taglist_returntype(self):
        l = tagweed.innermain({})
        self.assertIsInstance(l, list)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
