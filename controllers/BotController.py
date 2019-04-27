from bot_commands import BotCommands
from controllers.ServerController import ServerController
from helpers.CommandRequest import CommandRequest
from helpers.CommandResponse import CommandResponse


class BotController:

    def analyze_message(self, message):
        request = CommandRequest(message)

        try:
            command_name = request.message.split(' ')[0]
            command = BotCommands.COMMANDS[command_name]
            params = request.message.replace(command_name, '').strip()

            result = command.apply(params, request.channel_id, request.sender_id)
            self.send_result(result, request)

        except:
            self.send_error(request)

    def send_result(self, result, request):
        response = CommandResponse(request, result)
        ServerController().send_response(response)

    def send_error(self, request):
        error = "No pude entender tu mensaje. Utilizá el comando help para saber cómo puedo ayudarte."
        response = CommandResponse(request, error)
        ServerController().send_response(response)
