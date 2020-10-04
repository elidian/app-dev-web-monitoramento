from app import db
from app.models.cam_model import Cam, CamSchema

class CamService:   
    @staticmethod
    def get_cam_list():
        cams = Cam.query.order_by(Cam.id.asc()).all()
        cam_schema = CamSchema()
        return [cam_schema.dump(cam) for cam in cams]
    
    @staticmethod
    def get_cam_to_id(cam_id):
        cam = Cam.query.filter(Cam.id==cam_id).first()
        cam_schema = CamSchema()
        return cam_schema.dump(cam)
    
    @staticmethod
    def get_cam_to_name(camname):
        cam = Cam.query.filter(Cam.camname==camname).first()
        if not cam:
            return False
        cam_schema = CamSchema()
        return cam_schema.dump(cam)
    
    @staticmethod
    def set_cam(camname, email, password):
        cam = Cam(camname, email, password)
        db.session.add(cam)
        db.session.commit()
        cam_schema = CamSchema()
        return cam_schema.dump(cam)
    
    @staticmethod
    def delete_cam(cam_id):
        cam = Cam.query.filter(Cam.id==cam_id).first()
        if not cam:
            return False

        db.session.delete(cam)
        db.session.commit()
        cam_schema = CamSchema()
        return cam_schema.dump(cam)
    
    @staticmethod
    def put_cam(cam_id, jsonn):
        cam = Cam.query.filter(Cam.id==cam_id).first()
        if not cam:
            return False

        if jsonn['camname']:
            if Cam.query.filter(Cam.camname==jsonn['camname']).first():
                return False
            Cam.camname = jsonn['camname']
        if jsonn['email']:
            Cam.email = jsonn['email']
        if jsonn['password']:
            if jsonn['password_old'] and Cam.password_hash == Cam.set_password(jsonn['password_old']):
                Cam.password_hash = Cam.set_password(jsonn['password'])
            else:
                return False

        db.session.add(cam)
        db.session.commit()
        
        cam_schema = CamSchema()
        return cam_schema.dump(cam)