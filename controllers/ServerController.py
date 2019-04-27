import requests


class ServerController:
    # BASE_URL = 'https://slack-taller2.herokuapp.com'
    BASE_URL = 'http://localhost:3000'  # TODO remove this
    TIMEOUT = 180

    def send_response(self, response):
        url = f'{self.BASE_URL}/bots/messages'
        self._post(url, response.get_data())

    def get_user(self, user_id):
        url = f'{self.BASE_URL}/users/{user_id}'
        return self._get(url)

    def get_channel(self, channel_id):
        url = f'{self.BASE_URL}/channels/{channel_id}'
        return self._get(url)

    def get_channel_users(self, channel_id):
        url = f'{self.BASE_URL}/channels/{channel_id}/users'
        return self._get(url)

    def get_channel_statistics(self, channel_id):
        url = f'{self.BASE_URL}/channels/{channel_id}/statistics'
        return self._get(url)

    # private methods

    def _get(self, url):
        response = requests.get(url, timeout=self.TIMEOUT)
        return response.json()

    def _post(self, url, data):
        requests.post(url, json=data, timeout=self.TIMEOUT)
