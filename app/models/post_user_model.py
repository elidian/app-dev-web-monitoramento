from app import db
from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class PostUser(db.Model):
    __tablename__ = 'postuser'
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('cam.id'), index=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), index=True)

    def __repr__(self):
        return '<id: {}, user: {}, vehicle: {}, info: {}, time: {}>'.format(self.id, self.user_id, self.vehicle_id, self.body, self.timestamp)

    def __init__(self, info, user_id, vehicle_id):
        self.info = info
        self.timestamp = datetime.utcnow()
        self.user_id = user_id
        self.vehicle_id = vehicle_id

class PostUserSchema(SQLAlchemySchema):
    class Meta:
        model = PostUser
        load_instance = True
    
    id = auto_field()
    info = auto_field()
    timestamp = auto_field()
    user_id = auto_field()
    vehicle_id = auto_field()
