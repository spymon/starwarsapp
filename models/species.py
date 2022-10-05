from models.settings import db


class Specie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Specie_name = db.Column(db.String, unique=True)
