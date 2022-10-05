from models.settings import db


class SensorColor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensorColor = db.Column(db.String, unique=True)
