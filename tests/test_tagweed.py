#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_tagweed
----------------------------------

Tests for `tagweed` module.
"""
from __future__ import unicode_literals
from __future__ import absolute_import

import unittest
from requests.exceptions import HTTPError

from tagweed import tagweed


#
# class TestDoSessionGet(unittest.TestCase):
#     @mock.patch('requests.get')
#     def test_should_mock_session_get(self, get_mock):
#         get_mock.status_code = mock.MagicMock(get=mock.MagicMock(return_value=401))
#         #self.assertEqual(tagweed.innermain({'taggeturl':'https://api.pinboard.in/v1/tags/get?format=json','userid':'', 'password':''}), '{}')
#         with self.assertRaises(HTTPError) as cm:
#             #self.assertRaises(HTTPError, tagweed.innermain({'taggeturl':'https://api.pinboard.in/v1/tags/get?format=json','userid':'', 'password':''}), '{}')
#             tagweed.innermain({'taggeturl':'https://api.pinboard.in/v1/tags/get?format=json','userid':'', 'password':''})

class TestTagweed(unittest.TestCase):

    def setUp(self):
        self.baseline_dtags = {}
        self.baseline_dtags['abc'] = '0'
        self.baseline_dtags['def'] = '0'
        self.baseline_dtags['ghi'] = '0'
        self.baseline_dtags['jkl'] = '0'

    def test_similarity_not_similar(self):
        '''
        Test that we don't get false positives
        when looking for similar tags but we
        don't have any
        '''
        dtags = self.baseline_dtags
        dsims = tagweed.find_similar_tags(dtags, 0.8)
        self.assertEqual(len(dsims), 0)

    def test_similarity_when_similar(self):
        '''
        Test that we don't get false negatives
        '''
        dtags = self.baseline_dtags
        dtags['abcd'] = '0'
        dsims = tagweed.find_similar_tags(dtags, 0.8)
        self.assertEqual(len(dsims), 2)

    def test_similarity_when_plural(self):
        '''
        Test that we can isolate tags whose only
        difference is that they are plurals of a
        singular key
        '''
        dtags = self.baseline_dtags
        dtags['abcs'] = '0'
        dtags['defx'] = '0'
        dplurals = tagweed.find_plural_tags(dtags)
        self.assertEqual(len(dplurals), 1)

    def test_similarity_when_not_plural(self):
        '''
        Test that we don't get false positives
        when looking for tags that differ only
        because they are plural and we don't
        have any that fit that description.
        '''
        dtags = self.baseline_dtags
        dplurals = tagweed.find_plural_tags(dtags)
        self.assertEqual(len(dplurals), 0)

    def test_no_auth_handling(self):
        '''
        Test how the code deals with improper authorisation
        '''
        with self.assertRaises(HTTPError) as cm:   # noqa
            tagweed.innermain({'taggeturl': 'https://api.pinboard.in/v1/tags/get?format=json',
                               'source': 'PINBOARD',
                               'userid': '',
                               'password': ''})

    def test_local_handling(self):
        '''
        Test how the code deals with an attempt to use local
        '''
        with self.assertRaises(NotImplementedError) as cm:   # noqa

            tagweed.innermain({'taggeturl': 'https://api.pinboard.in/v1/tags/get?format=json',
                               'source': 'LOCAL',
                               'userid': '',
                               'password': ''})

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
