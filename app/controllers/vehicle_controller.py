from flask import Flask, json, jsonify, make_response, request, abort
from app import app
from app.services.vehicle_service import VehicleService as service
from flask_login import login_required

@app.route('/api/v1/vehicle')
def index_vehicle():
    return jsonify("Hi Vehicle, Welcome to Monitoramento API in Flask!")

@app.route('/api/v1/vehicles', methods=['GET'])
#@login_required
def get_vehicles():
    vehicles = service.get_vehicle_list()
    if not vehicles:
        abort(404)
    return jsonify(vehicles)
    
    

@app.route('/api/v1/vehicle/<int:vehicle_id>', methods=['GET'])
#@login_required
def get_vehicle(vehicle_id):
    vehicle = service.get_vehicle_to_id(vehicle_id)
    if not vehicle:
        abort(404)

    return jsonify(vehicle)

@app.route('/api/v1/vehicle/placa/<string:placa>', methods=['GET'])
#@login_required
def get_vehicle_to_placa(placa):
    vehicle = service.get_vehicle_to_placa(placa)
    if not vehicle:
        abort(404)

    return jsonify(vehicle)

''' json model
    {
        "placa": "PLA2020",
        "chassi": "321654987321",
        "cpf_dono": "12345678999",
        "queixa_roubo": false or true,
        "licenciamento": false or true,
        "exercicio": "2020",
        "ipva": false or true
    }
    '''
@app.route('/api/v1/vehicle/new', methods=['POST'])
#@login_required
def create_vehicle():
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
    
    placa = request.json['placa']
    chassi = request.json['chassi']
    cpf_dono = request.json['cpf_dono']
    queixa_roubo = request.json['queixa_roubo']
    licenciamento = request.json['licenciamento']
    exercicio = request.json['exercicio']
    ipva = request.json['ipva']
    
    vehicle = service.set_vehicle(placa, chassi, cpf_dono, queixa_roubo, licenciamento, exercicio, ipva)

    return jsonify(vehicle), 201

@app.route('/api/v1/vehicle/<int:vehicle_id>', methods=['DELETE'])
#@login_required
def delete_vehicle(vehicle_id):
    vehicle = service.delete_vehicle(vehicle_id)
    if not vehicle:
        abort(404)

    return jsonify(vehicle), 200

''' json model
    {
        "placa": "" or null,
        "chassi": "" or null,
        "cpf_dono": "" or null,
        "queixa_roubo": false or true or null,
        "licenciamento": false or true or null,
        "exercicio": "" or null,
        "ipva": false or true or null
    }
    '''
@app.route('/api/v1/vehicle/<int:vehicle_id>', methods=['PUT'])
#@login_required
def put_vehicle(vehicle_id):
    if not request.get_json():
        return jsonify("Requisição incompleta"), 400
    vehicle = service.put_vehicle(vehicle_id, request.get_json())
    if not vehicle:
        abort(404)
    
    return jsonify(vehicle), 200

@app.errorhandler(404)
def not_found_404(error):
    return make_response(jsonify({'error': 'Not found (404)'}), 404)
