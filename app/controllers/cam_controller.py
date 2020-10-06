from flask import Flask, json, jsonify, make_response, request, abort
from app import app
from app.services.cam_service import CamService as service
from flask_login import login_required

@app.route('/api/v1/cam')
def index_cam():
    return jsonify("Hi Cam, Welcome to Monitoramento API in Flask!")

@app.route('/api/v1/cams', methods=['GET'])
#@login_required
def get_cams():
    cams = service.get_cam_list()
    if not cams:
        abort(404)
    
    return jsonify(cams), 200

@app.route('/api/v1/cam/<int:cam_id>', methods=['GET'])
#@login_required
def get_cam(cam_id):
    cam = service.get_cam_to_id(cam_id)
    if not cam:
        abort(404)

    return jsonify(cam), 200

@app.route('/api/v1/user/cpf/<string:name>', methods=['GET'])
#@login_required
def get_user_to_name(name):
    cam = service.get_user_to_name(name)
    if not cam:
        abort(404)

    return jsonify(cam), 200

''' json model to create_cam()
    {
        "camname": "",
        "end": "",
        "password": ""
    }
    '''
@app.route('/api/v1/cam/new', methods=['POST'])
#@login_required
def create_cam():
    camname = request.json['camname']
    end = request.json['end']
    password = request.json['password']
    cam = service.set_cam(camname, end, password)

    return jsonify(cam), 201

@app.route('/api/v1/cam/<int:cam_id>', methods=['DELETE'])
#@login_required
def delete_cam(cam_id):
    cam = service.delete_cam(cam_id)
    if not cam:
        abort(404)

    return jsonify(cam), 200

''' json model to put_cam(cam_id)
    {
        "camname": "" or null,
        "email": "" or null,
        "password": "" or null,
        "password_old": "" or null
    }
    '''
@app.route('/api/v1/cam/<int:cam_id>', methods=['PUT'])
#@login_required
def put_cam(cam_id):
    if not request.get_json():
        return jsonify("Requisição incompleta"), 400
    cam = service.put_cam(cam_id, request.get_json())
    if cam is False:
        abort(404)
    if not cam:
        abort(404)
    return jsonify(cam), 200

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error 404': 'Not found'}), 404)

@app.errorhandler(403)
def not_found(error):
    return make_response(jsonify({'error 403': 'camname nao permitido'}), 403)
