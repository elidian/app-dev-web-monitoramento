from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(7), index=True, unique=True)
    chassi = db.Column(db.String(17), index=True, unique=True)
    cpf_dono = db.Column(db.String(11))
    queixa_roubo = db.Column(db.Boolean, index=True)
    licenciamento = db.Column(db.Boolean, index=True)
    exercicio = db.Column(db.String, index=True)
    ipva = db.Column(db.Boolean, index=True)

    def __repr__(self):
        return '<Vehicle Placa: {}; Chassi: {}; Cpf registrado: {}; Queixa de ROUBO: {}; ipva: {}; Licenciamento: {}; Exercicio: {}>'.format(self.placa, self.chassi, self.cpf_dono, self.queixa_roubo, self.ipva, self.licenciamento, self.exercicio)

    def check_is_placa(self, placa):
        if placa is not None:
            if (placa[0].isalpha() and placa[1].isalpha() and placa[2].isalpha() and placa[3].isdecimal() and (placa[4].isdecimal() or placa[4].isalpha()) and placa[5].isdecimal() and placa[6].isdecimal()) is False:
                return False

class UserCam(User):
    pass

class UserAgent(User):
    pass

class PostAgent(Post):
    pass

class PostCam(Post):
    pass

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
