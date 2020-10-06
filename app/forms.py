# formulários de login e registro de usuário
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models.user_model import User
from app.models.cam_model import Cam

class LoginForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    name = StringField('User name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    cpf = StringField('Cpf', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, name):
        user = User.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
        return True
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
        return True
    
    def validate_cpf(self, cpf):
        user = User.query.filter_by(cpf=cpf.data).first()
        if user is not None:
            raise ValidationError('Please use a different cpf.')
        return True

class RegistrationCamForm(FlaskForm):
    name = StringField('Cam name', validators=[DataRequired()])
    end = StringField('Endereco', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register Cam')

    def validate_name(self, name):
        cam = Cam.query.filter_by(name=name.data).first()
        if cam is not None:
            raise ValidationError('Please use a different camname.')
        return True
