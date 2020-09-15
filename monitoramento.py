from app import app, db
from app.old_models import PostAgent, PostCam, UserAgent, UserCam
from app.models.user_model import User
from app.models.post_model import Post
from app.models.vehicle_model import Vehicle

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'Vehicle': Vehicle, 'UserAgent': UserAgent, 'UserCam': UserCam, 'PostAgent': PostAgent, 'PostCam': PostCam}

if __name__ == '__main__':
    app.run(debug=True)
