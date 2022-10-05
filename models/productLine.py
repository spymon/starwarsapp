from models.settings import db


class ProductLine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ProductLine = db.Column(db.String, unique=True)
