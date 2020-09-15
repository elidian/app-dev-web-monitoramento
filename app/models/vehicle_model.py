from app import db
from datetime import datetime

class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(7), index=True, unique=True)
    chassi = db.Column(db.String(17), index=True, unique=True)
    cpf_dono = db.Column(db.String(11), index=True)
    queixa_roubo = db.Column(db.Boolean, index=True)
    licenciamento = db.Column(db.Boolean)
    exercicio = db.Column(db.String)
    ipva = db.Column(db.Boolean)

    def __repr__(self):
        return '<Vehicle Placa: {}; Chassi: {}; Cpf registrado: {}; Queixa de ROUBO: {}; ipva: {}; Licenciamento: {}; Exercicio: {}>'.format(self.placa, self.chassi, self.cpf_dono, self.queixa_roubo, self.ipva, self.licenciamento, self.exercicio)

    def check_is_placa(self, placa):
        if placa is not None:
            if (placa[0].isalpha() and placa[1].isalpha() and placa[2].isalpha() and placa[3].isdecimal() and (placa[4].isdecimal() or placa[4].isalpha()) and placa[5].isdecimal() and placa[6].isdecimal()) is False:
                return False
