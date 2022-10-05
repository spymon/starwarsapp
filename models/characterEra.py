from models.settings import db


class CharacterEra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    character = db.relationship('Character')
    era_id = db.Column(db.Integer, db.ForeignKey('era.id'))
    era = db.relationship('Era')

