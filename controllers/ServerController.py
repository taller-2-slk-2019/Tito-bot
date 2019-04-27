import requests


class ServerController:
    # BASE_URL = 'https://slack-taller2.herokuapp.com'
    BASE_URL = 'http://localhost:3000'  # TODO remove this
    TIMEOUT = 180

    def send_response(self, response):
        url = f'{self.BASE_URL}/bots/messages'
        requests.post(url, json=response.get_data(), timeout=self.TIMEOUT)

    def get_user(self, user_id):
        url = f'{self.BASE_URL}/users/{user_id}'
        response = requests.get(url, timeout=self.TIMEOUT)
        return response.json()
