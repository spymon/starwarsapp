from models.settings import db


class CharacterHomeworld(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    character = db.relationship('Character')
    homeworld_id = db.Column(db.Integer, db.ForeignKey('homeworld.id'))
    homeworld = db.relationship('Homeworld')

