from flask import Flask, json, jsonify, make_response, request, abort
from app import app, db
from app.models.vehicle_model import Vehicle, VehicleSchema

@app.route('/api/v1/vehicle')
def index_vehicle():
    return jsonify("Hi Vehicle, Welcome to Monitoramento API in Flask!")

@app.route('/api/v1/vehicles', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.order_by(Vehicle.id.asc()).all()
    if not vehicles:
        abort(404)
    
    vehicle_schema = VehicleSchema()
    return json.dumps([vehicle_schema.dump(vehicle) for vehicle in vehicles])

@app.route('/api/v1/vehicle/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    vehicle = Vehicle.query.filter(Vehicle.id==vehicle_id).first()
    if not vehicle:
        return jsonify("nenhuma Vehicle encontrado com esse id"), 204

    vehicle_schema = VehicleSchema()
    return json.dumps(vehicle_schema.dump(vehicle)), 200

''' json model
    {
        "placa": "",
        "chassi": "",
        "cpf_dono": "",
        "queixa_roubo": "",
        "licenciamento": "",
        "exercicio": "",
        "ipva": ""
    }
    '''
@app.route('/api/v1/vehicle/new', methods=['POST'])
def create_vehicle():
    #'''
    if not request.get_json():
        return jsonify("Requisição incompleta (json)"), 400
    
    if not request.json['placa']:
        return jsonify("Requisição incompleta (placa)"), 400
    if not request.json['chassi']:
        return jsonify("Requisição incompleta (chassi)"), 400
    if not request.json['cpf_dono']:
        return jsonify("Requisição incompleta (cfp_dono)"), 400
    if not json.dumps(request.json['queixa_roubo']):
        return jsonify("Requisição incompleta (queixa_roubo)"), 400
    if not json.dumps(request.json['licenciamento']):
        return jsonify("Requisição incompleta (licenciamento)"), 400
    if not request.json['exercicio']:
        return jsonify("Requisição incompleta (exercicio)"), 400
    if not json.dumps(request.json['ipva']):
        return jsonify("Requisição incompleta (ipva)"), 400
    #'''
    placa = request.json['placa']
    chassi = request.json['chassi']
    cpf_dono = request.json['cpf_dono']
    queixa_roubo = request.json['queixa_roubo']
    licenciamento = request.json['licenciamento']
    exercicio = request.json['exercicio']
    ipva = request.json['ipva']
    
    vehicle = Vehicle(placa, chassi, cpf_dono, queixa_roubo, licenciamento, exercicio, ipva)

    db.session.add(vehicle)
    db.session.commit()
    
    vehicle_schema = VehicleSchema()
    return json.dumps(vehicle_schema.dump(vehicle)), 201

@app.route('/api/v1/vehicle/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    vehicle = Vehicle.query.filter(Vehicle.id==vehicle_id).first()
    if not vehicle:
        return jsonify("nenhum Vehicle encontrado com esse id"), 204

    db.session.delete(vehicle)
    db.session.commit()
    vehicle_schema = VehicleSchema()
    return json.dumps(vehicle_schema.dump(vehicle)), 200

@app.route('/api/v1/vehicle/<int:vehicle_id>', methods=['PUT'])
def put_vehicle(vehicle_id):
    vehicle = Vehicle.query.filter(Vehicle.id==vehicle_id).first()
    if not vehicle:
        return jsonify("nenhum Vehicle encontrado com esse id"), 204
    if not request.get_json():
        return jsonify("Requisição incompleta"), 400
    
    if request.json['placa']:
        vehicle.placa = request.json['placa']
    if request.json['chassi']:
        vehicle.chassi = request.json['chassi']
    if request.json['cpf_dono']:
        vehicle.cpf_dono = request.json['cpf_dono']
    if request.json['queixa_roubo']:
        vehicle.queixa_roubo = request.json['queixa_roubo']
    if request.json['licenciamento']:
        vehicle.licenciamento = request.json['licenciamento']
    if request.json['exercicio']:
        vehicle.exercicio = request.json['exercicio']
    if request.json['ipva']:
        vehicle.ipva = request.json['ipva']

    db.session.add(vehicle)
    db.session.commit()
    
    vehicle_schema = VehicleSchema()
    return json.dumps(Vehicle_schema.dump(vehicle)), 200

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found (404)'}), 404)
