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

        return Rest(self._application_id).get(url, kwargs)

    def get_photo_stats(self, id):
        url = self._api_url + '/photos/' + id + '/stats'

        return Rest(self._application_id).get(url)

    def get_random_photo(self, **kwargs):
        url = self._api_url + '/photos/random'

        return Rest(self._application_id).get(url, kwargs)