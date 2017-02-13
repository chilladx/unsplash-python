# A unofficial Python wrapper for the Unsplash API.
#
# GitHub: https://github.com/michael-hacker/unsplash-python
# Author: Michael Hacker <mh@superchic.at>

from .rest import Rest


class Search(object):
    def __init__(self, settings):
        self._application_id = settings['application_id']

    def users(self, query, page=1, per_page=10):
        url = '/search/users'

        params = {
            'query': query,
            'page': page,
            'per_page': per_page
        }

        return Rest(self._application_id).get(url, params)

    def photos(self, query, page=1, per_page=10):
        url = '/search/photos'

        params = {
            'query': query,
            'page': page,
            'per_page': per_page
        }

        return Rest(self._application_id).get(url, params)

    def collections(self, query, page=1, per_page=10):
        url = '/search/collections'

        params = {
            'query': query,
            'page': page,
            'per_page': per_page
        }

        return Rest(self._application_id).get(url, params)