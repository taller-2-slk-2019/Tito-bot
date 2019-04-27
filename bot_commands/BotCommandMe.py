from dateutil.parser import *
from controllers.ServerController import ServerController


class BotCommandMe:

    def apply(self, params, channel_id, sender_id):
        user = ServerController().get_user(sender_id)
        result = ''

        result += f'Usuario: {user["username"]}\n'
        result += f'Nombre: {user["name"]}\n'
        result += f'Email: {user["email"]}\n'
        result += f'Se unió el {parse(user["createdAt"]).strftime("%d/%m/%Y")}\n'

        return result
