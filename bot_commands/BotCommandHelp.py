from bot_commands import BotCommands


class BotCommandHelp:

    def apply(self, params, channel_id, sender_id):
        commands = BotCommands.DESCRIPTIONS
        result = 'Estos son los comandos que entiendo: \n'

        for (command, description) in commands.items():
            result += f'  - {command}: {description}\n'

        return result

