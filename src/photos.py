"""
    GitHub: https://github.com/michael-hacker/unsplash-python
    Author: Michael Hacker <mh@superchic.at>
"""

from .rest import Rest


class Photos(object):
    def __init__(self, settings):
        self._application_id = settings['application_id']
        self._api_url        = settings['api_url']

    def list_photos(self, **kwargs):
        url = self._api_url + '/photos'

        return Rest(self._application_id).get(url, kwargs)

    def list_curated_photos(self, **kwargs):
        url = self._api_url + '/photos/curated'

        return Rest(self._application_id).get(url, kwargs)

    def search_photos(self, **kwargs):
        url = self._api_url + '/search/photos'

        return Rest(self._application_id).get(url, kwargs)

    def get_photo(self, id, **kwargs):
        url = self._api_url + '/photos/' + id

        query = {
            'w'    : kwargs.get('width', ''),
            'h'    : kwargs.get('height', ''),
            'rect' : kwargs.get('rectangle', '')
        }

        return Rest(self._application_id).get(url, query)

    def get_photo_stats(self, id):
        url = self._api_url + '/photos/' + id + '/stats'

        return Rest(self._application_id).get(url)

    def get_random_photo(self, **kwargs):
        url = self._api_url + '/photos/random'

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