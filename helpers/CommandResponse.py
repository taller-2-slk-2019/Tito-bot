class CommandResponse:

    def __init__(self, request, result):
        self.request = request
        self.result = result

    def get_data(self):
        return {
            'channelId': self.request.channel_id,
            'message': self.result,
            'bot': self.request.bot_name
        }