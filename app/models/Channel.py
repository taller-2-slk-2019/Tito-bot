from app import db


class Channel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    enabled = db.Column(db.DateTime)
