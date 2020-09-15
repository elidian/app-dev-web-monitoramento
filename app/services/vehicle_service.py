from app import db
from app.models.vehicle_model import Vehicle, VehicleSchema
from flask import jsonify

class VehicleService:
    @staticmethod
    def get_vehicle_id(placa):
        if not Vehicle.check_is_placa(placa):
            return False
        vehicle = Vehicle.query.filter(Vehicle.placa==placa).first()
        if not vehicle:
            return False
        return vehicle.id
            