from werkzeug.security import safe_str_cmp
from app.models.user_model import User

def authenticate(username, password):
    user = User.query.filter(User.username==username).first()
    if user and safe_str_cmp(user.password_hash, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User.query.filter(User.id==user_id).first()