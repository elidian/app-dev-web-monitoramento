#instacia do app Flask
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
ma = Marshmallow(app)

migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from app import controllers, models
from .controllers import user_controller, cam_controller, vehicle_controller, post_user_controller, post_cam_controller