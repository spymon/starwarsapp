from models.settings import db


class Degree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    degree_name = db.Column(db.String, unique=True)
