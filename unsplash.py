"""
    A unofficial Python wrapper for the Unsplash API.
    
    GitHub: https://github.com/michael-hacker/unsplash-python
    Author: Michael Hacker <mh@superchic.at>
"""

from .src.rest   import Rest
from .src.auth   import Auth
from .src.users  import Users
from .src.photos import Photos


class Unsplash(object):
    def __init__(self, settings):
        self._settings = {
            'callback_url'   : settings.get('callback_url'),
            'api_url'        : 'https://api.unsplash.com',
            'application_id' : settings.get('application_id')
        }

    def auth(self):
        return Auth(self._settings)

    def users(self):
        return Users(self._settings)

    def photos(self):
        return Photos(self._settings)

