class ChannelRequest:

    def __init__(self, data):
        self.bot_name = data['bot']
        self.channel_id = data['channelId']
        self.user_id = data['userId']
