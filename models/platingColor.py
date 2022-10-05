from models.settings import db


class PlatingColor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    platingColor = db.Column(db.String, unique=True)
