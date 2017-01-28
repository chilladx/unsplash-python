import json

from urllib.request import urlopen
from urllib.error   import URLError, HTTPError

class Unsplash(object):
    def __init__(self, settings):
        self._api_url        = 'https://api.unsplash.com/'
        self._application_id = settings['application_id']

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

    def get_users_profile(self, username):
        url = self._api_url + 'users/' + username + '?client_id=' + self._application_id

        return self._get_json_data(url)

    def list_users_photos(self, username, page = 1, per_page = 10, order_by = 'latest'):
        url  = self._api_url + 'users/' + username + '/photos'
        url += '?page=' + str(page) + '&per_page=' + str(per_page) + '&order_by=' + order_by
        url += '&client_id=' + self._application_id

        return self._get_json_data(url)
    
    def list_users_likes(self, username, page = 1, per_page = 10, order_by = 'latest'):
        url  = self._api_url + 'users/' + username + '/collections'
        url += '?page=' + str(page) + '&per_page=' + str(per_page) + '&order_by=' + order_by
        url += '&client_id=' + self._application_id

        return self._get_json_data(url)

    def list_users_collections(self, username, page = 1, per_page = 10):
        url  = self._api_url + 'users/' + username + '/collections'
        url += '?page=' + str(page) + '&per_page=' + str(per_page)
        url += '&client_id=' + self._application_id

        return self._get_json_data(url)

    def list_photos(self, page = 1, per_page = 10, order_by = 'latest'):
        url  = self._api_url + 'photos/'
        url += '?page=' + str(page) + '&per_page=' + str(per_page) + '&order_by=' + order_by
        url += '&client_id=' + self._application_id

        return self._get_json_data(url)

    def list_curated_photos(self, page = 1, per_page = 10, order_by = 'latest'):
        url  = self._api_url + 'photos/curated/'
        url += '?page=' + str(page) + '&per_page=' + str(per_page) + '&order_by=' + order_by
        url += '&client_id=' + self._application_id

        return self._get_json_data(url)

    def search_photos(self, query, page = 1, per_page = 10):
        url  = self._api_url + 'search/photos/'
        url += '?query=' + query + '&page=' + str(page) + '&per_page=' + str(per_page)
        url += '&client_id=' + self._application_id

        return self._get_json_data(url)

    def get_photo(self, id= '', width = '', height= '', rectangle= ''):
        if not id:
            return 'The photo’s ID is required.'

        url  = self._api_url + 'photos/' + id
        url += '?w=' + str(width) + '&h=' + str(height) + '&rect=' + rectangle
        url += '&client_id=' + self._application_id

        return self._get_json_data(url)

    def get_photo_stats(self, id = ''):
        if not id:
            return 'The photo’s ID is required.'

        url  = self._api_url + 'photos/' + id + '/stats'
        url += '?client_id=' + self._application_id

        return self._get_json_data(url)

    def get_random_photo(self, collections = '', featured = '', username = '', query = '', 
                         width = '', height = '', orientation = '', count = 1):
        url  = self._api_url + 'photos/random'

        if count > 30:
            count = 30

        if collections:
            url += '?collections=' + collections + '&'
        elif query:
            url += '?query=' + query + '&'
        else:
            url += '?'

        url += 'featured=' + featured + '&username=' + username
        url += '&w=' + width + '&h=' + height

        if orientation:
            url += '&orientation=' + orientation

        url += '&count=' + str(count) + '&client_id=' + self._application_id

        return self._get_json_data(url)