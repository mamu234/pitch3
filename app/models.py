from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Pitch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(1000), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

class User(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250))
    first_name = db.Column(db.String(150))
    pitches = db.relationship('Pitch')
    
    



def __repr__(self):
     return '<Name %r>' % self.name