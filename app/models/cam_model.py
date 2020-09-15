from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class Cam(UserMixin, db.Model):
    __tablename__ = 'cam'
    id = db.Column(db.Integer, primary_key=True)
    camname = db.Column(db.String(64), index=True, unique=True)
    end = db.Column(db.String(120), index=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Id: {}, Cam {}, End: {}>'.format(self.id, self.camname, self.end)

    def __init__(self, camname, end, password):
        self.camname = camname
        self.end = end
        self.password_hash = self.set_password(password)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_cam(id):
    return Cam.query.get(int(id))

class CamSchema(SQLAlchemySchema):
    class Meta:
        model = Cam
        load_instance = True
    
    id = auto_field()
    camname = auto_field()
    end = auto_field()
