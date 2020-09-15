from app import app, db
from app.models.vehicle_model import Vehicle, VehicleScham
from flask import jsonify

class VehicleService:
    @service
    def get_vehicle_id(placa):
        if not Vehicle.check_is_placa(placa):
            return False
        vehicle = Vehicle.query.filter(Vehicle.placa==placa).first()
        if not vehicle:
            return False
        return vehicle.id
            