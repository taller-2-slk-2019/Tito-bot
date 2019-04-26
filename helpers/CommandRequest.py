class CommandRequest:

    def __init__(self, data):
        self.bot_name = data['bot']
        self.message = data['message']
        self.channel_id = data['channelId']
        self.sender_id = data['senderId']