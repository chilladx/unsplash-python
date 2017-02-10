# A unofficial Python wrapper for the Unsplash API.
#
# GitHub: https://github.com/michael-hacker/unsplash-python
# Author: Michael Hacker <mh@superchic.at>

from .src.rest import Rest
from .src.auth import Auth
from .src.users import CurrentUsers, Users
from .src.photos import Photos
from .src.collections import Collections


class Unsplash(object):
    def __init__(self, settings):
        self._settings = {
            'application_id': settings.get('application_id', ''),
            'secret': settings.get('secret', ''),
            'callback_url': settings.get('callback_url', '')
        }

    def auth(self):
        return Auth(self._settings)

    def current_users(self, access_token=None):
        return CurrentUsers(
            application_id=self._settings['application_id'],
            access_token=access_token,
        )

    def users(self):
        return Users(self._settings)

    def photos(self):
        return Photos(self._settings)

    def collections(self):
        return Collections(self._settings)
