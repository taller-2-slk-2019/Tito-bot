from bot_commands.BotCommandHelp import BotCommandHelp
from bot_commands.BotCommandInfo import BotCommandInfo
from bot_commands.BotCommandMe import BotCommandMe
from bot_commands.BotCommandMute import BotCommandMute



COMMANDS = {
    'me': BotCommandMe(),
    'info': BotCommandInfo(),
    'mute': BotCommandMute(),
    'help': BotCommandHelp()
}

DESCRIPTIONS = {
    'me': 'Muestra los comandos disponibles',
    'info': 'Muestra información del canal',
    'mute': 'Desactiva respuestas por n segundos',
    'help': 'Muestra información del usuario que envía el mensaje'
}
