# A unofficial Python wrapper for the Unsplash API.
#
# GitHub: https://github.com/michael-hacker/unsplash-python
# Author: Michael Hacker <mh@superchic.at>

from .rest import Rest


class Collections(object):
    def __init__(self, settings):
        self._application_id = settings['application_id']

    def list_collections(self, page=1, per_page=10):
        url = '/collections'

        params = {
            'page': page,
            'per_page': per_page
        }

        return Rest(self._application_id).get(url, params)

    def list_featured_collections(self, page=1, per_page=10):
        url = '/collections/featured'

        params = {
            'page': page,
            'per_page': per_page
        }

        return Rest(self._application_id).get(url, params)

    def list_curated_collections(self, page=1, per_page=10):
        url = '/collections/curated'

        params = {
            'page': page,
            'per_page': per_page
        }

        return Rest(self._application_id).get(url, params)

    def get_collection(self, id):
        url = '/collections/%s' % str(id)

        return Rest(self._application_id).get(url)

    def get_curated_collection(self, id):
        url = '/collections/curated/%s' % str(id)

        return Rest(self._application_id).get(url)

    def get_collection_photos(self, id, page=1, per_page=10):
        url = '/collections/%s/photos' % str(id)

        params = {
            'page': page,
            'per_page': per_page
        }

        return Rest(self._application_id).get(url, params)

    def get_curated_collection_photos(self, id, page=1, per_page=10):
        url = '/collections/curated/%s/photos' % str(id)

        params = {
            'page': page,
            'per_page': per_page
        }

        return Rest(self._application_id).get(url, params)

    def list_collections_related_collections(self, id):
        # Work in progress!
        return None

    def create_collection(self, title, description=None, private=False):
        # Work in progress
        return None

    def update_collection(self, title, description=None, private=False):
        # Work in progress
        return None

    def delete_collection(self, id):
        # Work in progress
        return None

    def add_photo_to_collection(self, collection_id, photo_id):
        # Work in progress
        return None

    def remove_photo_from_collection(self, collection_id, photo_id):
        # Work in progress
        return None