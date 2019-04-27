import requests

class ServerController:

    # BASE_URL = 'https://slack-taller2.herokuapp.com/bots/messages'
    BASE_URL = 'http://localhost:3000/bots/messages'

    def send_response(self, response):
        requests.post(self.BASE_URL, json=response.get_data())
