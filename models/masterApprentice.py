from datetime import datetime
from models.settings import db


class MasterApprentice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    master_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    master = db.relationship("Character")
    apprentice_id = db.Column(db.String, db.ForeignKey('character.id'))
    apprentice = db.relationship("Character")

