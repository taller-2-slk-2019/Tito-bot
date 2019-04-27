from helpers.DateParser import DateParser
from controllers.ServerController import ServerController


class BotCommandInfo:

    def apply(self, params, channel_id, sender_id):
        channel = ServerController().get_channel(channel_id)
        result = ''

        result += f'Canal: {channel["name"]}\n'
        result += f'Descripción: {channel["description"]}\n'
        result += f'Público: {"Si" if channel["isPublic"] else "No"}\n'
        result += f'Se creó el {DateParser.parse(channel["createdAt"])}\n'

        users = ServerController().get_channel_users(channel_id)
        result += f'Integrantes: \n'
        for user in users:
            result += f'  - {user["name"]}'

        return result
