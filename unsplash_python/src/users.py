# A unofficial Python wrapper for the Unsplash API.
#
# GitHub: https://github.com/michael-hacker/unsplash-python
# Author: Michael Hacker <mh@superchic.at>

from .rest import Rest


class CurrentUsers(object):
    def __init__(self, settings):
        self._application_id = settings['application_id']
        self._bearer_token = settings['bearer_token']

    def profile(self):
        url = '/me?access_token=%s' % self._bearer_token

        return Rest().get(url)

    def update_profile(self, options):
        # Work in progress!

        url = '/me'

        options['access_token'] = self._bearer_token

        return Rest().put(url, options)


class Users(object):
    def __init__(self, settings):
        self._application_id = settings['application_id']
 
    def profile(self, username):
        url = '/users/%s' % username

        return Rest(self._application_id).get(url)

    def photos(self, username, page=None, per_page=None, order_by=None):
        url = '/users/%s/photos' % username

        query = {
            'page': page,
            'per_page': per_page,
            'order_by': order_by
        }

        return Rest(self._application_id).get(url, query)

    def likes(self, username, page=None, per_page=None, order_by=None):
        url = '/users/%s/likes' % username

        query = {
            'page': page,
            'per_page': per_page,
            'order_by': order_by
        }

        return Rest(self._application_id).get(url, query)

    def collections(self, username, page=None, per_page=None):
        url = '/users/%s/collections' % username

        query = {
            'page': page,
            'per_page': per_page
        }

        return Rest(self._application_id).get(url, query)