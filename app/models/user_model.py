from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import json
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    serialize_only = ('id', 'username', 'email')

    #serialize_rules = ('-merchants')

    def __repr__(self):
        return '<Id: {}, User {}, Email: {}>'.format(self.id, self.username, self.email)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = self.set_password(password)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
'''
    @property
    def serializer(self):
        #return {'id':self.id, 'name':self.username, 'email':self.email}
        d = Serializer.serialize(self)
        del d['password_hash']
        return d
'''

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
    
    id = auto_field()
    username = auto_field()
    email = auto_field()

'''
from sqlalchemy.inspection import inspect

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    def serialize_list(l):
        return [m.serialize() for m in l]
'''