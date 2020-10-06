from app import app, db
from app.models.user_model import User
from app.models.cam_model import Cam
from app.models.post_cam_model import PostCam
from app.models.post_user_model import PostUser
from app.models.vehicle_model import Vehicle

def reiniciar_db():
    User.query.delete()
    Cam.query.delete()
    PostUser.query.delete()
    PostCam.query.delete()
    Vehicle.query.delete()