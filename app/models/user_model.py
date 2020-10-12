from app import db
from app.models.model import Model
from app.models.post_user_model import PostUser
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class User(Model):
    __tablename__ = 'user'
    cpf = db.Column(db.String(15), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('PostUser', backref='author', lazy='dynamic')
    account_type = db.Column(db.String(15), default='session_user')

    def __repr__(self):
        return '<Id: {}, User {}, Cpf {}, Email: {}>'.format(self.id, self.name, self.cpf, self.email)

    def __init__(self, name, cpf, email, password):
        self.name = name
        self.email = email
        self.cpf = cpf
        self.set_password(password)
        self.account_type = "session_user"
        
class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
    
    id = auto_field()
    name = auto_field()
    cpf = auto_field()
    email = auto_field()
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