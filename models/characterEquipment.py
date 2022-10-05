from models.settings import db


class CharacterEquipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    character = db.relationship('Character')
    equipment_id = db.Column(db.Integer, db.ForeignKey('equipment.id'))
    equipment = db.relationship('Equipment')

