"""
    GitHub: https://github.com/michael-hacker/unsplash-python
    Author: Michael Hacker <mh@superchic.at>
"""

from .rest import Rest


class Photos(object):
    def __init__(self, settings):
        self._application_id = settings['application_id']

    def list_photos(self, page = 1, per_page = 10, order_by = None):
        url = '/photos'

        query = {
            'page'     : page,
            'per_page' : per_page,
            'order_by' : order_by
        }

        return Rest(self._application_id).get(url, query)

    def list_curated_photos(self, page = 1, per_page = 10, order_by = None):
        url = '/photos/curated'

        query = {
            'page'     : page,
            'per_page' : per_page,
            'order_by' : order_by
        }

        return Rest(self._application_id).get(url, query)

    def search_photos(self, query, page = 1, per_page = 10):
        url = '/search/photos'

        query = {
            'query'     : query,
            'page'      : page,
            'per_page'  : per_page
        }

        return Rest(self._application_id).get(url, query)

    def get_photo(self, id, width = None, height = None, rectangle = None):
        url = '/photos/%s' % id

        query = {
            'w'    : width,
            'h'    : height,
            'rect' : rectangle
        }

        return Rest(self._application_id).get(url, query)

    def get_photo_stats(self, id):
        url = '/photos/%s/stats' % id

        return Rest(self._application_id).get(url)

    def get_random_photo(self, **kwargs):
        url = '/photos/random'

        query = {
            'collections' : kwargs.get('collections', ''),
            'featured'    : kwargs.get('featured', ''),
            'username'    : kwargs.get('username', ''),
            'query'       : kwargs.get('query', ''),
            'w'           : kwargs.get('width', ''),
            'h'           : kwargs.get('height', ''),
            'orientation' : kwargs.get('orientation', ''),
            'count'       : kwargs.get('count', '1')
        }

        return Rest(self._application_id).get(url, query)

    def upload_photo(self, photo):
        # Work in progress!
        return None

    def like_photo(self, id):
        # Work in progress!
        return None

    def unlike_photo(self, id):
        # Work in progress!
        return None