from models.settings import db


class Cybernetic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cybernetic_name = db.Column(db.String, unique=True)

