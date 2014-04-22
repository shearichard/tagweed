#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_tagweed
----------------------------------

Tests for `tagweed` module.
"""

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
        self.baseline_dtags[u'abc'] = u'0'
        self.baseline_dtags[u'def'] = u'0'
        self.baseline_dtags[u'ghi'] = u'0'
        self.baseline_dtags[u'jkl'] = u'0'

    def test_similarity_not_similar(self):
        '''
        Test that we don't get false positives
        '''
        dtags = self.baseline_dtags
        dsims, dplurals = tagweed.find_similar_tags(dtags, 0.8)
        self.assertEqual(len(dsims), 0)

    def test_similarity_when_similar(self):
        '''
        Test that we don't get false negatives
        '''
        dtags = self.baseline_dtags
        dtags[u'abcd'] = u'0'
        dsims, dplurals = tagweed.find_similar_tags(dtags, 0.8)
        self.assertEqual(len(dsims), 2)

    def test_similarity_when_plural(self):
        '''
        Test that we can isolate tags whose only
        difference is that they are plurals of a
        singular key
        '''
        dtags = self.baseline_dtags
        dtags[u'abcs'] = u'0'
        dtags[u'defx'] = u'0'
        dsims, dplurals = tagweed.find_similar_tags(dtags, 0.8)
        self.assertEqual(len(dplurals), 1)

    def test_no_auth_handling(self):
        '''
        Test how the code deals with improper authorisation
        '''
        with self.assertRaises(HTTPError) as cm:
            tagweed.innermain({'taggeturl': 'https://api.pinboard.in/v1/tags/get?format=json',
                               'source': 'PINBOARD',
                               'userid': '',
                               'password': ''})

    def test_local_handling(self):
        '''
        Test how the code deals with an attempt to use local
        '''
        with self.assertRaises(NotImplementedError) as cm:
            tagweed.innermain({'taggeturl': 'https://api.pinboard.in/v1/tags/get?format=json',
                               'source': 'LOCAL',
                               'userid': '',
                               'password': ''})

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
