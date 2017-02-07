"""
    A unofficial Python wrapper for the Unsplash API.

    GitHub: https://github.com/michael-hacker/unsplash-python
    Author: Michael Hacker <mh@superchic.at>
"""

from unsplash_python.src.rest        import Rest
from unsplash_python.src.auth        import Auth
from unsplash_python.src.collections import Collections
from unsplash_python.src.users       import CurrentUsers, Users
from unsplash_python.src.photos      import Photos


class Unsplash(object):
    def __init__(self, settings):
        self._settings = {
            'application_id' : settings.get('application_id'),
            'secret'         : settings.get('secret'),
            'callback_url'   : settings.get('callback_url'),
            'bearer_token'   : settings.get('bearer_token')
        }

    def auth(self):
        return Auth(self._settings)

    def current_users(self):
        return CurrentUsers(self._settings)

    def users(self):
        return Users(self._settings)

    def photos(self):
        return Photos(self._settings)

    def collections(self):
        return Collections(self._settings)
