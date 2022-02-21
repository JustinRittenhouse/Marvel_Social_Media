from app import db
from datetime import datetime

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    comics_appeared_in = db.Column(db.Integer)
    super_power = db.Column(db.String)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f'<Character: {self.id} {self.user_id}>'