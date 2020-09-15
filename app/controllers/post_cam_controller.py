from flask import Flask, json, jsonify, make_response, request, abort
from app import app, db
from app.models.post_cam_model import PostCam, PostCamSchema
from app.services.vehicle_service import VehicleService

@app.route('/api/v1/cam/post')
def index_cam_post():
    return jsonify("Hi post, Welcome to Monitoramento API in Flask!")

@app.route('/api/v1/cam/posts', methods=['GET'])
def get_cam_posts():
    posts = PostCam.query.order_by(PostCam.id.asc()).all()
    if not posts:
        abort(404)
    
    post_schema = PostCamSchema()
    return json.dumps([post_schema.dump(post) for post in posts])

@app.route('/api/v1/cam/post/<int:post_id>', methods=['GET'])
def get_cam_post(post_id):
    post = PostCam.query.filter(PostCam.id==cam_id).order_by(PostCam.timestamp.asc()).all()
    if not cam:
        return jsonify("nenhum post encontrado com esse id"), 204

    post_schema = PostCamSchema()
    return json.dumps(post_schema.dump(post)), 200

''' json model
    {
        "info": "",
        "cam_id": "",
        "placa": ""
    }
    '''
@app.route('/api/v1/cam/post/new', methods=['POST'])
def create_cam_post():
    if not request.get_json():
        return jsonify("Requisição incompleta (json)"), 400
    if not request.json['info']:
        return jsonify("Requisição incompleta (info)"), 400
    if not request.json['cam_id']:
        return jsonify("Requisição incompleta (cam_id)"), 400
    if not request.json['placa']:
        return jsonify("Requisição incompleta (placa)"), 400
    
    info = request.json['info']
    cam_id = request.json['cam_id']
    placa = request.json['placa']
    
    vehicle_id = VehicleService.get_vehicle_id(placa)
    if not vehicle_id:
        return jsonify({"Erro: placa error"}), 400

    post = PostCam(info, cam_id, vehicle_id)

    db.session.add(post)
    db.session.commit()
    
    post_schema = PostCamSchema()
    return json.dumps(post_schema.dump(post)), 201

@app.route('/api/v1/cam/post/<int:post_id>', methods=['DELETE'])
def delete_cam_post(post_id):
    post = PostCam.query.filter(PostCam.id==post_id).first()
    if not post:
        return jsonify("nenhum post_cam encontrado com esse id"), 204

    db.session.delete(post)
    db.session.commit()

    post_schema = PostCamSchema()
    return json.dumps(post_schema.dump(post)), 200

@app.route('/api/v1/cam/post/<int:cam_id>', methods=['PUT'])
def put_cam_post(post_id):
    post = PostCam.query.filter(PostCam.id==post_id).first()
    if not post:
        return jsonify("nenhum post_cam encontrado com esse id"), 204
    if not request.get_json():
        return jsonify("Requisição incompleta"), 400
    
    if request.json['info']:
        cam.info = request.json['info']
    if request.json['cam_id']:
        cam.cam_id = request.json['cam_id']
    if request.json['vehicle_id']:
        cam.vehicle_id = request.json['vehicle_id']

    db.session.add(post)
    db.session.commit()

    post_schema = PostCamSchema()
    return json.dumps(post_schema.dump(post)), 200

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found (404)'}), 404)
