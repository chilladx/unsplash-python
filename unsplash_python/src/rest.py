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

    def _get_params(self, params):
        if params:
            params = { key: value for key, value in params.items() if value }
        else:
            params = {}

        if self._application_id:
            params['client_id'] = self._application_id

        params = { key: value for key, value in params.items() if value }

        return params

    def get(self, url, params=None):
        if params:
            params = self._get_params(params)

        url = '%s%s' % (self._api_url, url)

        try:
            response = requests.get(url, params=params)
        except Exception as e:
            logger.error('Connection error %s' %e)

        return response.json()

    def put(self, url, params={}):
        # TODO

        return False