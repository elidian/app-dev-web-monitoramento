from app import db
from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

class PostCam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    cam_id = db.Column(db.Integer, db.ForeignKey('cam.id'), index=True)
    vehicle_id = dbColumn(db.Integer, db.ForeignKey('vehicle.id'), index=True)

    def __repr__(self):
        return '<id: {}, cam: {}, vehicle: {}, info: {}, time: {}>'.format(self.id, self.cam_id, self.vehicle_id, self.body, self.timestamp)


class PostCamSchema(SQLAlchemySchema):
    class Meta:
        model = PostCam
        load_instance = True
    
    id = auto_field()
    info = auto_field()
    timestamp = auto_field()
    cam_id = auto_field()
