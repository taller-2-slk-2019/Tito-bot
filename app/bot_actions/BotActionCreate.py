from app.controllers.ServerController import ServerController


class BotActionCreate:

    def channel_created(self, user_id):
        if user_id:
            name = ServerController().get_user(user_id)["name"]
        else:
            name = "El administrador"

        result = f'{name} ha creado el canal'
        return result

    def conversation_created(self, user_id):
        user = ServerController().get_user(user_id)

        result = f'{user["name"]} ha iniciado la conversación'
        return result
