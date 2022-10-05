from models.settings import db


class Homeworld(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    homeworld = db.Column(db.String, unique=True)
