from models.settings import db


class CharacterArmament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    character = db.relationship('Character')
    armament_id = db.Column(db.Integer, db.ForeignKey('armament.id'))
    armament = db.relationship('Armament')

