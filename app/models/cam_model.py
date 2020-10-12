from app import db
from app.models.model import Model
from app.models.post_cam_model import PostCam
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class Cam(Model):
    __tablename__ = 'cam'
    end = db.Column(db.String(120), index=True)
    posts = db.relationship('PostCam', backref='author', lazy='dynamic')
    account_type = db.Column(db.String(15), default='session_cam')

    def __repr__(self):
        return '<Id: {}, Cam {}, End: {}>'.format(self.id, self.name, self.end)

    def __init__(self, name, end, password):
        self.name = name
        self.end = end
        self.set_password(password)
        self.account_type = "session_cam"
        
class CamSchema(SQLAlchemySchema):
    class Meta:
        model = Cam
        load_instance = True
    
    id = auto_field()
    name = auto_field()
    end = auto_field()
    account_type = auto_field()
    posts = auto_field()
'''
from app import login
from app.models.cam_model import Cam
from app.models.user_model import User
from flask import session

@login.user_loader
def load_user(id):
    if session['account_type'] == 'session_user':
        return User.query.get(int(id))
    elif session['account_type'] == 'session_cam':
        return Cam.query.get(int(id))
    else:
        print ('erro')
        return None
'''