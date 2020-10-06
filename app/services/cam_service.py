from app import db
from flask import json
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
    def get_cam_to_name(name):
        return Cam.query.filter(Cam.name==name).first()

    @staticmethod
    def get_cam_name(cam_id):
        cam = Cam.query.filter(Cam.id==cam_id).first()
        return cam.name

    @staticmethod
    def get_cam_to_name(name):
        cam = Cam.query.filter(Cam.name==name).first()
        if not cam:
            return False
        cam_schema = CamSchema()
        return cam_schema.dump(cam)
    
    @staticmethod
    def set_cam(name, email, password):
        cam = Cam(name, email, password)
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

        if jsonn['name']:
            if Cam.query.filter(Cam.name==jsonn['name']).first():
                return False
            Cam.name = jsonn['name']
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