"""
    GitHub: https://github.com/michael-hacker/unsplash-python
    Author: Michael Hacker <mh@superchic.at>
"""

import logging

from urllib.parse   import urlencode
from urllib.request import Request, urlopen

from .rest import Rest

logger = logging.getLogger('unsplash-python')

class Auth(object):
    def __init__(self, settings):
        self._application_id = settings['application_id']
        self._callback_url   = settings['callback_url']
        self._secret         = settings['secret']
        self._oauth_url      = 'https://unsplash.com/oauth/authorize'

    def authentication_url(self, scope = ''):
        if scope:
            scope = ' '.join([item for item in scope])

        query = {
            'client_id'     : self._application_id,
            'redirect_uri'  : self._callback_url,
            'response_type' : 'code',
            'scope'         : scope
        }

        url = self._oauth_url + '?' + urlencode(query)

        return url

    def user_authentication(self, code = ''):

        query = {
            'client_id'     : self._application_id,
            'client_secret' : self._secret,
            'redirect_uri'  : self._callback_url,
            'code'          : code,
            'grant_type'    : 'authorization_code'
        }

        request = Request('https://unsplash.com/oauth/token', urlencode(query).encode())

        return urlopen(request).read().decode()