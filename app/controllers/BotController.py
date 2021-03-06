from app.bot_actions.BotActionCreate import BotActionCreate
from app.bot_actions.BotActionWelcome import BotActionWelcome
from app.bot_commands import BotCommands
from app.controllers.ServerController import ServerController
from app.helpers.CommandRequest import CommandRequest
from app.helpers.CommandResponse import CommandResponse
from app.helpers.ChannelRequest import ChannelRequest
from app.helpers.ConversationRequest import ConversationRequest
from app.models import Channel
from datetime import datetime


class BotController:

    def analyze_message(self, message):
        request = CommandRequest(message)
        channel = Channel.query.filter_by(id=request.channel_id).first()

        if channel is not None and channel.enabled > datetime.now():
            return

        try:
            command_name = request.message.split(' ')[0]
            command = BotCommands.COMMANDS[command_name]
            params = request.message.replace(command_name, '').strip()

            result = command.apply(params, request.channel_id, request.sender_id)
            self.send_result(result, request)

        except:
            self.send_error(request)

    def welcome_user(self, data):
        request = ChannelRequest(data)
        result = BotActionWelcome().apply(request.channel_id, request.user_id)
        self.send_result(result, request)

    def create_channel(self, data):
        request = ChannelRequest(data)
        result = BotActionCreate().channel_created(request.user_id)
        self.send_result(result, request)

    def create_conversation(self, data):
        request = ConversationRequest(data)
        result = BotActionCreate().conversation_created(request.user_id)
        self.send_result(result, request)

    def send_result(self, result, request):
        response = CommandResponse(request, result)
        ServerController().send_response(response)

    def send_error(self, request):
        error = "No pude entender tu mensaje. Utilizá el comando help para saber cómo puedo ayudarte."
        response = CommandResponse(request, error)
        ServerController().send_response(response)
