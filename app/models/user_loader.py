from app import db, login
from app.models.cam_model import Cam
from app.models.user_model import User
from flask import session

@login.user_loader
def load_user(id):
    if session['account_type'] == 'session_user':
        return User.query.get(int(id))
    elif session['account_type'] == 'session_cam':
        return Cam.query.get(int(id))
    else:
        print ('erro')
        return None
