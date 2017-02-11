#!/usr/bin/env python3

import unittest

import vcr

from config import UnsplashTestCase
from unsplash_python.unsplash import Unsplash


class Photos(UnsplashTestCase):
    vcr_path = 'tests/vcr/photos/'

    @vcr.use_cassette(vcr_path + 'list_photos.json')
    def test_list_photos(self):
        response = self.unsplash.photos().list_photos(
            per_page=2
        )
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(len(response), 2)

    @vcr.use_cassette(vcr_path + 'list_curated_photos.json')
    def test_list_curated_photos(self):
        response = self.unsplash.photos().list_curated_photos(
            per_page=2
        )
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(len(response), 2)

    @vcr.use_cassette(vcr_path + 'search_photos.json')
    def test_search_photos(self):
        response = self.unsplash.photos().search_photos(
            query='lisboa',
            per_page=2
        )
        self.assertIsInstance(response, dict)
        self.assertIsInstance(response.get('results'), list)
        self.assertEqual(len(response.get('results')), 2)

    @vcr.use_cassette(vcr_path + 'get_photo.json')
    def test_get_photo(self):
        response = self.unsplash.photos().get_photo(
            photo_id='3PmwYw2uErY'
        )
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get('id'), '3PmwYw2uErY')

    @vcr.use_cassette(vcr_path + 'get_photo_stats.json')
    def test_get_photo_stats(self):
        response = self.unsplash.photos().get_photo_stats(
            photo_id='3PmwYw2uErY'
        )
        self.assertIsInstance(response, dict)

    @vcr.use_cassette(vcr_path + 'get_random_photo.json')
    def test_get_random_photo(self):
        response = self.unsplash.photos().get_random_photo(
            username='michael_hacker',
            count=2
        )
        self.assertIsInstance(response, list)
        self.assertEqual(len(response), 2)


if __name__ == "__main__":
    unittest.main()
