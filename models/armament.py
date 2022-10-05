from models.settings import db


class Armament(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    armament_name = db.Column(db.String, unique=True)

