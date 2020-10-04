from flask import Flask, json, jsonify, make_response, request, abort
from app import app
from app.services.user_service import UserService as service

@app.route('/api/v1/user')
def index_user():
    return jsonify("Hi User, Welcome to Monitoramento API in Flask!")

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    users = service.get_user_list()
    if not users:
        abort(404)
    
    return jsonify(users), 200

@app.route('/api/v1/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = service.get_user_to_id(user_id)
    if not user:
        abort(404)

    return jsonify(user), 200

@app.route('/api/v1/user/cpf/<string:cpf>', methods=['GET'])
def get_user_to_cpf(cpf):
    user = service.get_user_to_cpf(cpf)
    if not user:
        abort(404)

    return jsonify(user), 200

''' json model
    {
        "username": "",
        "cpf": "",
        "email": "",
        "password": ""
    }
    '''
@app.route('/api/v1/user/new', methods=['POST'])
def create_user():
    username = request.json['username']
    cpf = request.json['cpf']
    email = request.json['email']
    password = request.json['password']
    user = service.set_user(username, cpf, email, password)

    return jsonify(user), 201

@app.route('/api/v1/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = service.delete_user(user_id)
    if not user:
        abort(404)

    return jsonify(user), 200

''' json model to put_user(user_id)
    {
        "username": "" or null,
        "cpf": "" or null,
        "email": "" or null,
        "password": "" or null,
        "password_old": "" or null
    }
    '''
@app.route('/api/v1/user/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    if not request.get_json():
        return jsonify("Requisição incompleta"), 400
    user = service.put_user(user_id, request.get_json())
    if user is False:
        abort(403)
    if not user:
        abort(404)
    return jsonify(user), 200

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error 404': 'Not found'}), 404)

@app.errorhandler(403)
def not_found(error):
    return make_response(jsonify({'error 403': 'CPF nao permitido'}), 403)
