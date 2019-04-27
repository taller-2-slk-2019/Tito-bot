import http

from flask import Flask, request

from controllers.BotController import BotController

app = Flask(__name__)


@app.route('/')
def index():
    return 'Bot Tito'


@app.route('/bot', methods=["POST"])
def bot():
    data = request.get_json()
    BotController().analyze_message(data)
    return '', http.HTTPStatus.NO_CONTENT


@app.route('/welcome', methods=["POST"])
def welcome():
    data = request.get_json()
    BotController().welcome_user(data)
    return '', http.HTTPStatus.NO_CONTENT


if __name__ == '__main__':
    app.run()
