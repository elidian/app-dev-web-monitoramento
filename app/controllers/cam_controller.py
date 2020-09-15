from flask import Flask, json, jsonify, make_response, request, abort
from app import app, db
from app.models.cam_model import Cam, CamSchema

@app.route('/api/v1/cam')
def index_cam():
    return jsonify("Hi Cam, Welcome to Monitoramento API in Flask!")

@app.route('/api/v1/cams', methods=['GET'])
def get_cams():
    cams = Cam.query.order_by(Cam.id.asc()).all()
    if not cams:
        abort(404)
    
    cam_schema = CamSchema()
    return json.dumps([cam_schema.dump(cam) for cam in cams])

@app.route('/api/v1/cam/<int:cam_id>', methods=['GET'])
def get_cam(cam_id):
    cam = Cam.query.filter(Cam.id==cam_id).first()
    if not cam:
        return jsonify("nenhuma CAM encontrado com esse id"), 204

    cam_schema = CamSchema()
    return json.dumps(cam_schema.dump(cam)), 200

@app.route('/api/v1/cam/new', methods=['POST'])
def create_cam():
    camname = request.json['camname']
    end = request.json['end']
    password = request.json['password']
    cam = Cam(camname, end, password)

    db.session.add(cam)
    db.session.commit()
    
    cam_schema = CamSchema()
    return json.dumps(cam_schema.dump(cam)), 201

@app.route('/api/v1/cam/<int:cam_id>', methods=['DELETE'])
def delete_cam(cam_id):
    cam = Cam.query.filter(Cam.id==cam_id).first()
    if not cam:
        return jsonify("nenhum cam encontrado com esse id"), 204

    db.session.delete(cam)
    db.session.commit()
    cam_schema = CamSchema()
    return json.dumps(cam_schema.dump(cam)), 200

@app.route('/api/v1/cam/<int:cam_id>', methods=['PUT'])
def put_cam(cam_id):
    cam = Cam.query.filter(Cam.id==cam_id).first()
    if not cam:
        return jsonify("nenhum Cam encontrado com esse id"), 204
    if not request.get_json():
        return jsonify("Requisição incompleta"), 400
    
    if request.json['camname']:
        cam.camname = request.json['camname']
    if request.json['end']:
        cam.end = request.json['end']
    if request.json['password']:
        cam.senha = request.json['password']

    db.session.add(cam)
    db.session.commit()
    
    cam_schema = CamSchema()
    return json.dumps(cam_schema.dump(cam)), 200

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error 404': 'Not found'}), 404)
