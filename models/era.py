from models.settings import db


class Era(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    era_name = db.Column(db.String, unique=True)
