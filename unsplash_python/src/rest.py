# A unofficial Python wrapper for the Unsplash API.
#
# GitHub: https://github.com/michael-hacker/unsplash-python
# Author: Michael Hacker <mh@superchic.at>

import logging

import requests

logger = logging.getLogger('unsplash-python')


class Rest(object):
    def __init__(self, application_id=None, access_token=None):
        self._application_id = application_id
        self._access_token = access_token
        self._api_url = 'https://api.unsplash.com'

    def get(self, url, params={}):
        result = None
        params = {key: value for key, value in params.items() if value}

        if self._application_id:
            params['client_id'] = self._application_id

        url = '%s%s' % (self._api_url, url)

        try:
            response = requests.get(url, params=params)
        except Exception as errors:
            logger.error('Connection error %s' % errors)

        try:
            if response.status_code == 200:
                result = response.json()
            else:
                errors = response.json().get('errors')
                logger.error('Connection error %s' % errors)
        except ValueError:
            result = None

        return result

    def put(self, url, params={}):
        result = None
        params = {key: value for key, value in params.items() if value}

        headers = {
            'Authorization': 'Bearer %s' % self._access_token,
            'Accept-Version': 'v1'
        }

        url = '%s%s' % (self._api_url, url)

        try:
            response = requests.put(url, params=params, headers=headers)
        except Exception as errors:
            logger.error('Connection error %s' % errors)

        try:
            if response.status_code == 200:
                result = response.json()
            else:
                errors = response.json().get('errors')
                logger.error('Connection error %s' % errors)
        except ValueError:
            result = None

        return result
