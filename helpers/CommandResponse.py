class CommandResponse:

    def __init__(self, request, result):
        self.request = request
        self.result = result

    def get_data(self):
        return {
            'channelId': getattr(self.request, 'channel_id', None),
            'conversationId': getattr(self.request, 'conversation_id', None),
            'message': self.result,
            'bot': self.request.bot_name
        }