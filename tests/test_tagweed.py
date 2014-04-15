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
        pass

    def test_no_auth_handling(self):
        '''
        Test how the code deals with improper authorisation
        '''
        with self.assertRaises(HTTPError) as cm:
            tagweed.innermain({'taggeturl': 'https://api.pinboard.in/v1/tags/get?format=json',
                               'userid': '',
                               'password': ''})

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
