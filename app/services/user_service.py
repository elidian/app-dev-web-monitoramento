from app import db
from app.models.user_model import User, UserSchema

class UserService:   
    @staticmethod
    def get_user_list():
        users = User.query.order_by(User.id.asc()).all()
        user_schema = UserSchema()
        return [user_schema.dump(user) for user in users]
    
    @staticmethod
    def get_user_to_id(user_id):
        user = User.query.filter(User.id==user_id).first()
        user_schema = UserSchema()
        return user_schema.dump(user)
    
    @staticmethod
    def get_user_to_placa(cpf):
        user = User.query.filter(User.cpf==cpf).first()
        if not user:
            return False
        user_schema = UserSchema()
        return user_schema.dump(user)
    
    @staticmethod
    def set_user(username, email, password):
        user = User(username, email, password)
        db.session.add(user)
        db.session.commit()
        user_schema = UserSchema()
        return user_schema.dump(user)
    
    @staticmethod
    def delete_user(user_id):
        user = User.query.filter(User.id==user_id).first()
        if not user:
            return False

        db.session.delete(user)
        db.session.commit()
        user_schema = UserSchema()
        return user_schema.dump(user)
    
    @staticmethod
    def put_user(user_id, jsonn):
        user = User.query.filter(User.id==user_id).first()
        if not user:
            return False

        if jsonn['username']:
            user.username = jsonn['username']
        if jsonn['cpf']:
            if User.query.filter(User.cpf==jsonn['cpf']).first():
                return False
            user.cpf = jsonn['cpf']
        if jsonn['email']:
            user.email = jsonn['email']
        if jsonn['password']:
            if jsonn['password_old'] and user.password_hash == User.set_password(jsonn['password_old']):
                user.password_hash = User.set_password(jsonn['password'])
            else:
                return False

        db.session.add(user)
        db.session.commit()
        
        user_schema = UserSchema()
        return user_schema.dump(user)