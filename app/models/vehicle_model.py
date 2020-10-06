from app import app, db
from datetime import datetime
from app.models.post_user_model import PostUser
from app.models.post_cam_model import PostCam
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(7), index=True, unique=True)
    chassi = db.Column(db.String(17), index=True, unique=True)
    cpf_dono = db.Column(db.String(11), index=True)
    queixa_roubo = db.Column(db.Boolean, index=True)
    licenciamento = db.Column(db.Boolean)
    exercicio = db.Column(db.String)
    ipva = db.Column(db.Boolean)
    posts_user = db.relationship('PostUser', backref='vehicle', lazy='dynamic')
    posts_cam = db.relationship('PostCam', backref='vehicle', lazy='dynamic')

    def __repr__(self):
        return '<id: {}, Vehicle Placa: {}; Chassi: {}; Cpf registrado: {}; Queixa de ROUBO: {}; Licenciamento: {}; Exercicio: {}; ipva: {}>'.format(self.id, self.placa, self.chassi, self.cpf_dono, self.queixa_roubo, self.licenciamento, self.exercicio, self.ipva)
    
    def __init__(self, placa, chassi, cpf_dono, queixa_roubo, licenciamento, exercicio, ipva):
        self.placa = placa
        self.chassi = chassi
        self.cpf_dono = cpf_dono
        self.queixa_roubo = queixa_roubo
        self.licenciamento = licenciamento
        self.exercicio = exercicio
        self.ipva = ipva
    
    def check_is_placa(placa):
        if placa:
            if (placa[0].isalpha() and placa[1].isalpha() and placa[2].isalpha() and placa[3].isdecimal() and (placa[4].isdecimal() or placa[4].isalpha()) and placa[5].isdecimal() and placa[6].isdecimal()):
                return True    
        return False

class VehicleSchema(SQLAlchemySchema):
    class Meta:
        model = Vehicle
        load_instance = True
    
    id = auto_field()
    placa = auto_field()
    chassi = auto_field()
    cpf_dono = auto_field()
    queixa_roubo = auto_field()
    licenciamento = auto_field()
    exercicio = auto_field()
    ipva = auto_field()
    posts_user = auto_field()
    posts_cam = auto_field()
