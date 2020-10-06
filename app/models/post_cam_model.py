from app import db
from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class PostCam(db.Model):
    __tablename__ = 'postcam'
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    cam_id = db.Column(db.Integer, db.ForeignKey('cam.id'), index=True)
    cam_name = db.Column(db.String(64), index=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicle.id'), index=True)
    vehicle_placa = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<id: {}, cam: {}, vehicle: {}, info: {}, time: {}>'.format(self.id, self.cam_id, self.cam_name, self.vehicle_id, self.vehicle_placa, self.body, self.timestamp)

    def __init__(self, info, cam_id, cam_name, vehicle_id, vehicle_placa):
        self.info = info
        self.timestamp = datetime.utcnow()
        self.cam_id = cam_id
        self.cam_name = cam_name
        self.vehicle_id = vehicle_id
        self.vehicle_placa = vehicle_placa

class PostCamSchema(SQLAlchemySchema):
    class Meta:
        model = PostCam
        load_instance = True
    
    id = auto_field()
    info = auto_field()
    timestamp = auto_field()
    cam_id = auto_field()
    cam_name = auto_field()
    vehicle_id = auto_field()
    vehicle_placa = auto_field()
