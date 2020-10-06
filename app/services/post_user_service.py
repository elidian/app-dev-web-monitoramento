from app import db
from app.models.post_user_model import PostUser, PostUserSchema
from app.services.vehicle_service import VehicleService
from app.services.user_service import UserService

class PostService:   
    @staticmethod
    def get_post_list():
        posts = PostUser.query.order_by(PostUser.id.asc()).all()
        if not posts:
            return False
        post_schema = PostUserSchema()
        return [post_schema.dump(post) for post in posts]
    
    @staticmethod
    def get_post_to_id(post_id):
        post = PostUser.query.filter(PostUser.id==post_id).first()
        if not post:
            return False
        post_schema = PostUserSchema()
        return post_schema.dump(post)
    
    @staticmethod
    def set_post(info, user_id, placa):
        if not UserService.get_user_to_id(user_id):
            return "user_error"
        vehicle = VehicleService.get_vehicle_to_placa(placa)
        if not vehicle:
            return "vehicle_error"
        name = UserService.get_user_name(user_id)
        post = PostUser(info, user_id, name, vehicle['id'], placa)
        db.session.add(post)
        db.session.commit()
        post_schema = PostUserSchema()
        return post_schema.dump(post)
    
    @staticmethod
    def delete_post(post_id):
        post = PostUser.query.filter(PostUser.id==post_id).first()
        if not post:
            return False

        db.session.delete(post)
        db.session.commit()
        post_schema = PostUserSchema()
        return post_schema.dump(post)

    @staticmethod
    def put_post(post_id, jsonn):
        post = PostUser.query.filter(PostUser.id==post_id).first()
        if not post:
            return False

        if jsonn['info']:
            post.info = jsonn['info']
        if jsonn['user_id']:
            if not UserService.get_user_to_id(jsonn['user_id']):
                return False
            post.user_id = jsonn['user_id']
            post.name = UserService.get_user_name(user_id)
        if jsonn['placa']:
            vehicle = VehicleService.get_vehicle_to_placa(jsonn['placa'])
            if not vehicle:
                return False
            post.vehicle_id = vehicle['id']
            post.placa = vehicle['placa']

        db.session.add(post)
        db.session.commit()

        post_schema = PostUserSchema()
        return post_schema.dump(post)
