"""
    GitHub: https://github.com/michael-hacker/unsplash-python
    Author: Michael Hacker <mh@superchic.at>
"""

from .rest import Rest


class Collections(object):
    def __init__(self, settings):
        self._application_id = settings['application_id']
        self._api_url        = settings['api_url']

    def list_collections(self, page = 1, per_page = 10, order_by = 'popular'):
        url = self._api_url + '/collections'

        query = {
            'page'     : page,
            'per_page' : per_page,
            'order_by' : order_by
        }

        return Rest(self._application_id).get(url, query)

    def list_curated_collections(self, page = 1, per_page = 10):
        url = self._api_url + '/collections/curated'

        query = {
            'page'     : page,
            'per_page' : per_page
        }

        return Rest(self._application_id).get(url, query)

    def list_featured_collections(self, page = 1, per_page = 10):
        url = self._api_url + '/collections/featured'

        query = {
            'page'     : page,
            'per_page' : per_page
        }

        return Rest(self._application_id).get(url, query)

    def get_collection(self, id):
        url = self._api_url + '/collections/' + str(id)

        return Rest(self._application_id).get(url)