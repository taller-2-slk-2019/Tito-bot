from app.bot_commands.BotCommandHelp import BotCommandHelp
from app.bot_commands.BotCommandInfo import BotCommandInfo
from app.bot_commands.BotCommandMe import BotCommandMe
from app.bot_commands.BotCommandMute import BotCommandMute



COMMANDS = {
    'me': BotCommandMe(),
    'info': BotCommandInfo(),
    'mute': BotCommandMute(),
    'help': BotCommandHelp()
}

DESCRIPTIONS = {
    'me': 'Muestra información del usuario que envía el mensaje',
    'info': 'Muestra información del canal',
    'mute <n>': 'Desactiva respuestas por n segundos',
    'help': 'Muestra los comandos disponibles'
}
