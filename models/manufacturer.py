from models.settings import db


class Manufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    manufacturer_name = db.Column(db.String, unique=True)
