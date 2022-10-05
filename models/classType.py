from models.settings import db


class ClassType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classtype_name = db.Column(db.String, unique=True)
