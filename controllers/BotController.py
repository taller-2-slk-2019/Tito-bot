from bot_commands.BotCommandHelp import BotCommandHelp
from bot_commands.BotCommandInfo import BotCommandInfo
from bot_commands.BotCommandMe import BotCommandMe
from bot_commands.BotCommandMute import BotCommandMute


class BotController:
    COMMANDS = {
        'me': BotCommandMe(),
        'info': BotCommandInfo(),
        'mute': BotCommandMute(),
        'help': BotCommandHelp()
    }

    def analyze_message(self, message):
        bot_name = message['bot']
        msg = message['message']
        channel_id = message['channelId']
        sender_id = message['senderId']

        try:
            command_name = msg.split()[0]
            command = self.COMMANDS[command_name]
            params = msg.replace(command_name).strip()

            result = command.apply(params, channel_id, sender_id)
            self.send_result(result, channel_id, bot_name)

        except:
            self.send_error(channel_id, bot_name)

    def send_result(self, result, channel_id, bot_name):
        # TODO result
        return

    def send_error(self, channel_id, bot_name):
        # TODO error
        return
