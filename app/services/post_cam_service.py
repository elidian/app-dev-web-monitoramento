from app import db
from app.models.post_cam_model import PostCam, PostCamSchema
from app.services.vehicle_service import VehicleService
from app.services.cam_service import CamService

class PostService:   
    @staticmethod
    def get_post_list():
        posts = PostCam.query.order_by(PostCam.id.asc()).all()
        if not posts:
            return False
        post_schema = PostCamSchema()
        return [post_schema.dump(post) for post in posts]
    
    @staticmethod
    def get_post_to_id(post_id):
        post = PostCam.query.filter(PostCam.id==post_id).first()
        if not post:
            return False
        post_schema = PostCamSchema()
        return post_schema.dump(post)
    
    @staticmethod
    def set_post(info, cam_id, placa):
        if not CamService.get_cam_to_id(cam_id):
            return "cam_error"
        vehicle = VehicleService.get_vehicle_to_placa(placa)
        if not vehicle:
            return "vehicle_error"
        name = CamService.get_cam_name(cam_id)
        post = PostCam(info, cam_id, name, vehicle['id'], placa)
        db.session.add(post)
        db.session.commit()
        post_schema = PostCamSchema()
        return post_schema.dump(post)
    
    @staticmethod
    def delete_post(post_id):
        post = PostCam.query.filter(PostCam.id==post_id).first()
        if not post:
            return False

        db.session.delete(post)
        db.session.commit()
        post_schema = PostCamSchema()
        return post_schema.dump(post)

    @staticmethod
    def put_post(post_id, jsonn):
        post = PostCam.query.filter(PostCam.id==post_id).first()
        if not post:
            return False

        if jsonn['info']:
            post.info = jsonn['info']
        if jsonn['cam_id']:
            if not CamService.get_cam_to_id(jsonn['cam_id']):
                return False
            post.cam_id = jsonn['cam_id']
            post.name = CamService.get_cam_name(cam_id)
        if jsonn['placa']:
            vehicle = VehicleService.get_vehicle_to_placa(jsonn['placa'])
            if not vehicle:
                return False
            post.vehicle_id = vehicle['id']
            post.placa = vehicle['placa']

        db.session.add(post)
        db.session.commit()

        post_schema = PostCamSchema()
        return post_schema.dump(post)
