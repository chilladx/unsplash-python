# A unofficial Python wrapper for the Unsplash API.
#
# GitHub: https://github.com/michael-hacker/unsplash-python
# Author: Michael Hacker <mh@superchic.at>

import logging

import requests

logger = logging.getLogger('unsplash-python')


class Rest(object):
    def __init__(self, application_id=None):
        self._application_id = application_id
        self._api_url = 'https://api.unsplash.com'

    def _get_header(self):
        return {
            'Authorization': 'Bearer %s' % '',
            'Accept-Version': 'v1'
        }

    def get(self, url, params={}):
        json = None
        params = { key: value for key, value in params.items() if value }

        if self._application_id:
            params['client_id'] = self._application_id


        url = '%s%s' % (self._api_url, url)

        try:
            response = requests.get(url, params=params)
            json = response.json()
        except Exception as e:
            logger.error('Connection error %s' %e)

        return json

    def put(self, url, params={}):
        # TODO

        return False