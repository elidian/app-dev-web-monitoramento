# configuração de chave secreta
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    print('\nLoad configurations ..\n')

    # active DEBUG
    DEBUG = True

    # configuração da chave secreta
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Desenvolvimento-Web-2020.1'

    # configuração do Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    
    # SQLAlchemy monitorará modificações de objetos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
