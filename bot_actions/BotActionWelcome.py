from controllers.ServerController import ServerController


class BotActionWelcome:

    def apply(self, channel_id, user_id):
        channel = ServerController().get_channel(channel_id)
        user = ServerController().get_user(user_id)

        result = f'{user["name"]} {channel["welcome"]}'
        return result
