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
    def __init__(self, application_id):
        self._application_id = application_id

    def get(self, url, query = {}):
        json_data          = None
        query['client_id'] = self._application_id

        if query:
            url += '?' + urlencode(query)

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
                'Reason: {}'.format(rror.reason)
            )

        return json_data