from models.settings import db


class CharacterCybernetic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    character = db.relationship('Character')
    cybernetic_id = db.Column(db.Integer, db.ForeignKey('cybernetic.id'))
    cybernetic = db.relationship('Cybernetic')

