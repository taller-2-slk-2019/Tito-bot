from helpers.DateParser import DateParser
from controllers.ServerController import ServerController


class BotCommandInfo:

    def apply(self, params, channel_id, sender_id):
        result = ''
        result += self._get_channel_info(channel_id)
        result += self._get_channel_statistics(channel_id)
        result += self._get_Channel_users(channel_id)

        return result

    def _get_channel_info(self, channel_id):
        channel = ServerController().get_channel(channel_id)
        result = ''

        result += f'Canal: {channel["name"]}\n'
        result += f'Descripción: {channel["description"]}\n'
        result += f'Público: {"Si" if channel["isPublic"] else "No"}\n'
        result += f'Se creó el {DateParser.parse(channel["createdAt"])}\n'

        return result

    def _get_Channel_users(self, channel_id):
        result = ''
        users = ServerController().get_channel_users(channel_id)

        result += f'Integrantes: \n'
        for user in users:
            result += f'  - {user["name"]}'

        return result

    def _get_channel_statistics(self, channel_id):
        result = ''
        stats = ServerController().get_channel_statistics(channel_id)

        result += f'Mensajes enviados: {stats["messageCount"]} \n'

        return result
