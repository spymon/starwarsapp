from models.settings import db


class FormerAffiliation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'))
    character = db.relationship('Character')
    affiliation_id = db.Column(db.Integer, db.ForeignKey('affiliation.id'))
    affiliation = db.relationship('Affiliation')

