from app import db
from app.models.user_model import User, UserSchema

class UserService:   
    @staticmethod
    def get_user_list():
        users = User.query.order_by(User.id.asc()).all()
        user_schema = UserSchema()
        return [user_schema.dump(user) for user in users]
    
    @staticmethod
    def get_user_to_id(id):
        user = User.query.filter(User.id==id).first()
        user_schema = UserSchema()
        return user_schema.dump(user)
    
    @staticmethod
    def get_user_to_name(name):
        return User.query.filter(User.name==name).first()

    @staticmethod
    def get_user_name(id):
        user = User.query.filter(User.id==id).first()
        return user.name
    
    @staticmethod
    def get_user_to_cpf(cpf):
        user = User.query.filter(User.cpf==cpf).first()
        if not user:
            return False
        user_schema = UserSchema()
        return user_schema.dump(user)
    
    @staticmethod
    def set_user(name, email, password):
        user = User(name, email, password)
        db.session.add(user)
        db.session.commit()
        user_schema = UserSchema()
        return user_schema.dump(user)
    
    @staticmethod
    def delete_user(id):
        user = User.query.filter(User.id==id).first()
        if not user:
            return False

        db.session.delete(user)
        db.session.commit()
        user_schema = UserSchema()
        return user_schema.dump(user)
    
    @staticmethod
    def put_user(id, jsonn):
        user = User.query.filter(User.id==id).first()
        if not user:
            return False

        if jsonn['name']:
            user.name = jsonn['name']
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
