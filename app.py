from flask import Flask, request
from controllers.BotController import BotController

app = Flask(__name__)


@app.route('/')
def index():
    return 'Bot Tito'


@app.route('/bot', methods=["POST"])
def bot():
    data = request.get_json()
    result = BotController().analyze_message(data)
    return str(result)


if __name__ == '__main__':
    app.run()
