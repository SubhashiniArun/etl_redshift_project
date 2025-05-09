from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class CityData(db.Model):
    __tablename__ = 'city_data'

    city = db.Column(db.String(255), primary_key=True)
    avg_value = db.Column(db.Float)
    first_seen = db.Column(db.DateTime)
    last_seen = db.Column(db.DateTime)