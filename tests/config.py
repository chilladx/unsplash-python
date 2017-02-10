#!/usr/bin/env python3

import os
import unittest

from unsplash_python.unsplash import Unsplash


class UnsplashTestCase(unittest.TestCase):
    def setUp(self):
        self.unsplash = Unsplash({
            'application_id': os.environ.get('application_id', ''),
            'secret': os.environ.get('secret', ''),
            'callback_url': '',
            'bearer_token': ''
        })