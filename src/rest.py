"""
    GitHub: https://github.com/michael-hacker/unsplash-python
    Author: Michael Hacker <mh@superchic.at>
"""

import logging
import json

from urllib.error   import URLError, HTTPError
from urllib.parse   import urlencode
from urllib.request import urlopen

logger = logging.getLogger('unsplash-python')


class Rest(object):
    def __init__(self, application_id = None):
        self._application_id = application_id
        self._api_url        = 'https://api.unsplash.com'

    def _request(self, url, method, query = None):
        json_data = None
        url       = '%s%s' % (self._api_url, url)

        if self._application_id:
            url += '?client_id=%s' % self._application_id

        if query:
            query = { key: value for key, value in query.items() if value }
            url += urlencode(query)

        #headers = self._get_auth_header()
        #headers.update(query)

        try:
            with urlopen(url) as response:
                body = response.read()

            json_data = json.loads(body.decode('utf-8'))

        except HTTPError as error:
            logger.error(
                'HTTP status {}'.format(error.code)
            )
        
        except URLError as error:
            logger.error(
                'Reason: {}'.format(error.reason)
            )

        return json_data

    # def _get_auth_header(self):
    #     return {
    #         'Authorization' : 'Bearer %s' % ''
    #     }

    def get(self, url, query = None):
        return self._request(url, 'get', query = query)

    def put(self, url, query = {}):
        # TODO

        return False