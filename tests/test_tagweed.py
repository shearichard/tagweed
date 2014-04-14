#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_tagweed
----------------------------------

Tests for `tagweed` module.
"""

import unittest

from tagweed import tagweed


class TestTagweed(unittest.TestCase):

    def setUp(self):
        pass

    def test_taglist_returntype(self):
        d = tagweed.innermain({})
        self.assertIsInstance(d, dict)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
