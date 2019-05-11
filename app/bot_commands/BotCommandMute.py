from app import db
from app.models import Channel
from datetime import datetime, timedelta
import random


class BotCommandMute:

    MAX_SECONDS = 3600

    def apply(self, params, channel_id, sender_id):
        seconds = self._get_seconds(params)
        if seconds > self.MAX_SECONDS:
            return f'Soy un bot muy responsable. No puedo irme por más de {self.MAX_SECONDS} segundos'
        if seconds <= 0:
            return f'Soy un bot muy inteligente y se que los segundos deben ser positivos'

        channel = Channel.query.filter_by(id=channel_id).first()
        if channel is None:
            channel = Channel(id=channel_id)

        channel.enabled = datetime.now() + timedelta(seconds=seconds)

        db.session.add(channel)
        db.session.commit()

        return self._get_message(seconds)

    def _get_message(self, seconds):
        messages = [f'No responderé mensajes por {seconds} segundos. No me extrañen.',
                    f'Me voy a dormir por {seconds} segundos. No me van a poder despertar.',
                    f'Soy muy vago y no voy a trabajar por {seconds} segundos. Igual no me pagan.',
                    f'Por qué me silencian por {seconds} segundos? No me quieren?',
                    f'Me quedaré callado por {seconds} segundos? Espero que no me reemplacen por otro bot']

        return random.choice(messages)

    def _get_seconds(self, params):
        return int(params)
