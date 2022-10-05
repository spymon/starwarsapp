from models.settings import db


class Affiliation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    affiliation_name = db.Column(db.String, unique=True)

