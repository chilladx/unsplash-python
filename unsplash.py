"""
    A unofficial Python wrapper for the Unsplash API.
    
    GitHub: https://github.com/michael-hacker/unsplash-python
    Author: Michael Hacker <mh@superchic.at>
"""

from .src.photos import Photos
from .src.rest   import Rest
from .src.users  import Users

class Unsplash(object):
    def __init__(self, settings):
        self._api_url        = 'https://api.unsplash.com'
        self._oauth_url      = 'https://unsplash.com/oauth/authorize'
        self._application_id = settings['application_id']
        self._callback_url   = settings['callback_url']

        self._settings = {
            'api_url'        : self._api_url,
            'application_id' : self._application_id
        }

    def get_authentication_url(self, scope = ''):
        if scope:
            scope = ' '.join([item for item in scope])

        query = {
            'redirect_uri'  : self._callback_url,
            'response_type' : 'code',
            'client_id'     : self._application_id,
            'scope'         : scope
        }

        url = self._oauth_url + '?' + urlencode(query)

        return url

    def users(self):
        return Users(self._settings)

    def photos(self):
        return Photos(self._settings)

