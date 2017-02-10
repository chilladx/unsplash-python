#!/usr/bin/env python3

import unittest

from config import UnsplashTestCase
from unsplash_python.unsplash import Unsplash


class Users(UnsplashTestCase):
    def test_profile(self):
        response = self.unsplash.users().profile(
            username='michael_hacker'
        )
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get('username'), 'michael_hacker')

    def test_photos(self):
        response = self.unsplash.users().photos(
            username='michael_hacker',
            per_page=2
        )
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(len(response), 2)

    def test_likes(self):
        response = self.unsplash.users().likes(
            username='michael_hacker',
            per_page=2
        )
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(len(response), 2)

    def test_collections(self):
        response = self.unsplash.users().collections(
            username='michael_hacker',
            per_page=2
        )
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(len(response), 2)


if __name__ == "__main__":
    unittest.main()