import json

from urllib.error   import URLError, HTTPError
from urllib.parse   import urlencode
from urllib.request import urlopen

class Unsplash(object):
    def __init__(self, settings):
        self._api_url        = 'https://api.unsplash.com'
        self._oauth_url      = 'https://unsplash.com/oauth/authorize'
        self._application_id = settings['application_id']
        self._callback_url   = settings['callback_url']

    def _get_json_data(self, url):
        try:
            with urlopen(url) as response:
                data = response.read()

            json_data = json.loads(data.decode('utf-8'))

        except HTTPError as error:
            json_data = url + ' (Error code: ' +  str(error.code) + ')'
        
        except URLError as error:
            json_data = 'Reason: ' +  error.reason

        return json_data

    def get_authentication_url(self, scope = ''):
        if scope:
            scope = ' '.join([item for item in scope])

        query = {
            'redirect_uri'  : self._callback_url,
            'response_type' : 'code',
            'client_id'     : self._application_id,
            'scope'         : scope
        }

        url = self._oauth_url + '?' + urlencode(query)

        return url

    def get_users_profile(self, username):
        url = self._api_url + '/users/' + username + '?'

        query = {
            'client_id' : self._application_id
        }

        return self._get_json_data(url + urlencode(query))

    def list_users_photos(self, username, page = 1, per_page = 10, order_by = 'latest'):
        url = self._api_url + '/users/' + username + '/photos?'

        query = {
            'page'      : page,
            'per_page'  : per_page,
            'order_by'  : order_by,
            'client_id' : self._application_id
        }

        return self._get_json_data(url + urlencode(query))
    
    def list_users_likes(self, username, page = 1, per_page = 10, order_by = 'latest'):
        url = self._api_url + '/users/' + username + '/collections?'

        query = {
            'page'      : page,
            'per_page'  : per_page,
            'order_by'  : order_by,
            'client_id' : self._application_id
        }

        return self._get_json_data(url + urlencode(query))

    def list_users_collections(self, username, page = 1, per_page = 10):
        url = self._api_url + '/users/' + username + '/collections?'

        query = {
            'page'      : page,
            'per_page'  : per_page,
            'client_id' : self._application_id
        }

        return self._get_json_data(url + urlencode(query))

    def list_photos(self, page = 1, per_page = 10, order_by = 'latest'):
        url = self._api_url + '/photos/?'

        query = {
            'page'      : page,
            'per_page'  : per_page,
            'order_by'  : order_by,
            'client_id' : self._application_id
        }

        return self._get_json_data(url + urlencode(query))

    def list_curated_photos(self, page = 1, per_page = 10, order_by = 'latest'):
        url  = self._api_url + '/photos/curated/?'

        query = {
            'page'      : page,
            'per_page'  : per_page,
            'order_by'  : order_by,
            'client_id' : self._application_id
        }

        return self._get_json_data(url + urlencode(query))

    def search_photos(self, query, page = 1, per_page = 10):
        url  = self._api_url + '/search/photos/?'

        query = {
            'query'     : query,
            'per_page'  : per_page,
            'client_id' : self._application_id
        }

        return self._get_json_data(url + urlencode(query))

    def get_photo(self, id= '', width = '', height= '', rectangle= ''):
        url = self._api_url + '/photos/' + id + '?'
        
        query = {
            'w'         : width,
            'h'         : height,
            'rect'      : rectangle,
            'client_id' : self._application_id
        }

        return self._get_json_data(url + urlencode(query))

    def get_photo_stats(self, id = ''):
        url = self._api_url + '/photos/' + id + '/stats?'
        
        query = {
            'client_id' : self._application_id
        }

        return self._get_json_data(url + urlencode(query))

    def get_random_photo(self, collections = '', featured = '', username = '', query = '', 
                         width = '', height = '', orientation = '', count = 1):
        url = self._api_url + '/photos/random?'

        query = {
            'featured'  : featured,
            'username'  : username,
            'w'         : width,
            'h'         : height,
            'count'     : count > 30 and 30 or count,
            'client_id' : self._application_id
        }

        if orientation:
            query['orientation'] = orientation

        if collections:
            query['collections'] = collections
        elif query:
            query['query'] = query

        return self._get_json_data(url + urlencode(query))
