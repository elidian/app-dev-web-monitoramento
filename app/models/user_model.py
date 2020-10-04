from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True)
    cpf = db.Column(db.String(15), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<Id: {}, User {}, Email: {}>'.format(self.id, self.username, self.email)

    def __init__(self, username, cpf, email, password):
        self.username = username
        self.email = email
        self.cpf = cpf
        self.set_password(password)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
    
    id = auto_field()
    username = auto_field()
    cpf = auto_field()
    email = auto_field()
