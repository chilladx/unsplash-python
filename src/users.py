"""
    GitHub: https://github.com/michael-hacker/unsplash-python
    Author: Michael Hacker <mh@superchic.at>
"""

import logging

from .rest import Rest

logger = logging.getLogger('unsplash-python')


class CurrentUsers(object):
    def __init__(self, settings):
        self._application_id = settings['application_id']
        self._bearer_token   = settings['bearer_token']
        self._api_url        = settings['api_url']

    def profile(self):
        url = self._api_url + '/me?access_token=' + self._bearer_token

        return Rest().get(url)

    def update_profile(self, **kwargs):
        # TODO

        url = self._api_url + '/me'

        kwargs['access_token'] = self._bearer_token

        return Rest().put(url, kwargs)


class Users(object):
    def __init__(self, settings):
        self._application_id = settings['application_id']
        self._api_url        = settings['api_url']
 
    def profile(self, username):
        url = self._api_url + '/users/' + username

        return Rest(self._application_id).get(url)

    def photos(self, username, **kwargs):
        url = self._api_url + '/users/' + username + '/photos'

        return Rest(self._application_id).get(url, kwargs)

    def likes(self, username, **kwargs):
        url = self._api_url + '/users/' + username + '/likes'

        return Rest(self._application_id).get(url, kwargs)

    def collections(self, username, **kwargs):
        url = self._api_url + '/users/' + username + '/collections'

        return Rest(self._application_id).get(url, kwargs)