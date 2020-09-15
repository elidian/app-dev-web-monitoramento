from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.models.user_model import User
from  app.models.post_model import Post

class UserCam(User):
    pass

class UserAgent(User):
    pass

class PostAgent(Post):
    pass

class PostCam(Post):
    pass

