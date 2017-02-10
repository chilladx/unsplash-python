# A unofficial Python wrapper for the Unsplash API.
#
# GitHub: https://github.com/michael-hacker/unsplash-python
# Author: Michael Hacker <mh@superchic.at>

import logging

import requests

logger = logging.getLogger('unsplash-python')


class Rest(object):
    def __init__(self, application_id=None, bearer_token=None):
        self._application_id = application_id
        self._bearer_token = bearer_token
        self._api_url = 'https://api.unsplash.com'

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
        json = None
        params = { key: value for key, value in params.items() if value }
        
        headers = {
            'Authorization': 'Bearer %s' % self._bearer_token,
            'Accept-Version': 'v1'
        }

        url = '%s%s' % (self._api_url, url)

        try:
            response = requests.put(url, params=params, headers=headers)
            json = response.json()
        except Exception as e:
            logger.error('Connection error %s' %e)

        return json