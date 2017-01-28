import json
import urllib

class Unsplash(object):
    def __init__(self, settings):
        self._api_url = 'https://api.unsplash.com/'
        self._application_id = settings['application_id']

    def _get_json_data(self, url):
        try:
            with urllib.request.urlopen(url) as response:
                data = response.read()

            json_data = json.loads(data.decode('utf-8'))

        except:
             json_data = False

        return json_data

    def get_users_profile(self, username):
        url = self._api_url + 'users/' + username + '?client_id=' + self._application_id

        return self._get_json_data(url)

    def get_users_photos(self, username, page = 1, per_page = 10, order_by = 'latest'):
        url  = self._api_url + 'users/' + username + '/photos?'
        url += url + '&page=' + str(page) + '&per_page=' + str(per_page) + '&order_by=' + order_by
        url += url + '&client_id=' + self._application_id

        return self._get_json_data(url)
    
    def get_users_likes(self, username, page = 1, per_page = 10, order_by = 'latest'):
        url  = self._api_url + 'users/' + username + '/collections?'
        url += url + '&page=' + str(page) + '&per_page=' + str(per_page) + '&order_by=' + order_by
        url += url + '&client_id=' + self._application_id

        return self._get_json_data(url)

    def get_users_collections(self, username, page = 1, per_page = 10):
        url  = self._api_url + 'users/' + username + '/collections?'
        url += url + '&page=' + str(page) + '&per_page=' + str(per_page)
        url += url + '&client_id=' + self._application_id

        return self._get_json_data(url)
