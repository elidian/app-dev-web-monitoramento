from app import db
from app.models.vehicle_model import Vehicle, VehicleSchema

class VehicleService:   
    @staticmethod
    def get_vehicle_list():
        vehicles = Vehicle.query.order_by(Vehicle.id.asc()).all()
        vehicle_schema = VehicleSchema()
        return [vehicle_schema.dump(vehicle) for vehicle in vehicles]

    @staticmethod
    def get_vehicle_to_id(vehicle_id):
        vehicle = Vehicle.query.filter(Vehicle.id==vehicle_id).first()
        vehicle_schema = VehicleSchema()
        return vehicle_schema.dump(vehicle)

    @staticmethod
    def get_vehicle_to_placa(placa):
        if not Vehicle.check_is_placa(placa):
            return False
        vehicle = Vehicle.query.filter(Vehicle.placa==placa).first()
        if not vehicle:
            return False
        vehicle_schema = VehicleSchema()
        return vehicle_schema.dump(vehicle)

    @staticmethod
    def set_vehicle(placa, chassi, cpf_dono, queixa_roubo, licenciamento, exercicio, ipva):
        vehicle = Vehicle(placa, chassi, cpf_dono, queixa_roubo, licenciamento, exercicio, ipva)
        db.session.add(vehicle)
        db.session.commit()
        vehicle_schema = VehicleSchema()
        return vehicle_schema.dump(vehicle)
    
    @staticmethod
    def delete_vehicle(vehicle_id):
        vehicle = Vehicle.query.filter(Vehicle.id==vehicle_id).first()
        if not vehicle:
            return False

        db.session.delete(vehicle)
        db.session.commit()
        vehicle_schema = VehicleSchema()
        return vehicle_schema.dump(vehicle)
    
    @staticmethod
    def put_vehicle(vehicle_id, jsonn):
        vehicle = Vehicle.query.filter(Vehicle.id==vehicle_id).first()
        if not vehicle:
            return False

        if jsonn['placa']:
            vehicle.placa = jsonn['placa']
        if jsonn['chassi']:
            vehicle.chassi = jsonn['chassi']
        if jsonn['cpf_dono']:
            vehicle.cpf_dono = jsonn['cpf_dono']
        if jsonn['queixa_roubo'] is not None:
            vehicle.queixa_roubo = jsonn['queixa_roubo']
        if jsonn['licenciamento'] is not None:
            vehicle.licenciamento = jsonn['licenciamento']
        if jsonn['exercicio']:
            vehicle.exercicio = jsonn['exercicio']
        if jsonn['ipva'] is not None:
            vehicle.ipva = jsonn['ipva']
        
        db.session.add(vehicle)
        db.session.commit()
    
        vehicle_schema = VehicleSchema()
        return vehicle_schema.dump(vehicle)