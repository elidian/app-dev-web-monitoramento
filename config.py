# configuração de chave secreta
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Desenvolvimento-Web-2020.1'