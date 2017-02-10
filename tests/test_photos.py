#!/usr/bin/env python3

import unittest

from config import UnsplashTestCase
from unsplash_python.unsplash import Unsplash


class AuthPhotos(UnsplashTestCase):
    def test_list_photos(self):
        response = self.unsplash.photos().list_photos(
            per_page=2
        )
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(len(response), 2)

    def test_list_curated_photos(self):
        response = self.unsplash.photos().list_photos(
            per_page=2
        )
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(len(response), 2)

    def test_search_photos(self):
        response = self.unsplash.photos().search_photos(
            query='lisboa',
            per_page=2
        )
        self.assertIsInstance(response, dict)
        self.assertIsInstance(response.get('results'), list)
        self.assertEqual(len(response.get('results')), 2)

    def test_get_photo(self):
        response = self.unsplash.photos().get_photo(
            id='3PmwYw2uErY'
        )
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get('id'), '3PmwYw2uErY')

    def test_get_photo_stats(self):
        response = self.unsplash.photos().get_photo_stats(
            id='3PmwYw2uErY'
        )
        self.assertIsInstance(response, dict)

    def test_get_random_photo(self):
        response = self.unsplash.photos().get_random_photo(
            username='michael_hacker',
            count=2
        )
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 2)


if __name__ == "__main__":
    unittest.main()