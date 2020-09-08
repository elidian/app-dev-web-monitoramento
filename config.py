# configuração de chave secreta
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # configuração da chave secreta
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Desenvolvimento-Web-2020.1'

    # configuração do Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
