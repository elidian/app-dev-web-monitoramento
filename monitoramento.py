from app import app, db
from app.models.user_model import User
from app.models.cam_model import Cam
from app.models.post_cam_model import PostCam
from app.models.post_user_model import PostUser
from app.models.vehicle_model import Vehicle
'''
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Vehicle': Vehicle, 'UserAgent': UserAgent, 'UserCam': UserCam, 'PostAgent': PostAgent, 'PostCam': PostCam}
'''
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'PostUser': PostUser, 'Vehicle': Vehicle, 'Cam': Cam, 'PostCam': PostCam}

if __name__ == '__main__':
    app.run(debug=True)
