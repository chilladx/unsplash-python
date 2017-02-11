#!/usr/bin/env python3

import unittest

import vcr

from config import UnsplashTestCase
from unsplash_python.unsplash import Unsplash


class Collections(UnsplashTestCase):
    @vcr.use_cassette('tests/vcr/list_collections.json')
    def test_list_collections(self):
        response = self.unsplash.collections().list_collections(
            per_page=2
        )
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(len(response), 2)

    @vcr.use_cassette('tests/vcr/list_featured_collections.json')
    def test_list_featured_collections(self):
        response = self.unsplash.collections().list_featured_collections(
            per_page=2
        )
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(len(response), 2)

    @vcr.use_cassette('tests/vcr/list_curated_collections.json')
    def test_list_curated_collections(self):
        response = self.unsplash.collections().list_curated_collections(
            per_page=2
        )
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(len(response), 2)

    @vcr.use_cassette('tests/vcr/get_collection.json')
    def test_get_collection(self):
        response = self.unsplash.collections().get_collection(
            id=446398
        )
        self.assertIsInstance(response, dict)
        self.assertEqual(response.get('id'), 446398)

    @vcr.use_cassette('tests/vcr/get_curated_collection.json')
    def test_get_curated_collection(self):
        response = self.unsplash.collections().get_curated_collection(
            id=134
        )
        self.assertIsInstance(response, dict)

    @vcr.use_cassette('tests/vcr/get_collection_photos.json')
    def test_get_collection_photos(self):
        response = self.unsplash.collections().get_collection_photos(
            id=446398,
            per_page=2
        )
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)
        self.assertEqual(len(response), 2)

    @vcr.use_cassette('tests/vcr/get_curated_collection_photos.json')
    def test_get_curated_collection_photos(self):
        response = self.unsplash.collections().get_curated_collection_photos(
            id=134
        )
        self.assertIsInstance(response, list)
        self.assertIsInstance(response[0], dict)


if __name__ == '__main__':
    unittest.main()
