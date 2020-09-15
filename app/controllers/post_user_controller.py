from flask import Flask, json, jsonify, make_response, request, abort
from app import app, db
from app.models.post_user_model import PostUser, PostUserSchema
from app.services.vehicle_service import VehicleService

@app.route('/api/v1/user/post')
def index_user_post():
    return jsonify("Hi post, Welcome to Monitoramento API in Flask!")

@app.route('/api/v1/user/posts', methods=['GET'])
def get_user_posts():
    posts = PostUser.query.order_by(PostUser.id.asc()).all()
    if not posts:
        return jsonify(""), 204
    
    post_schema = PostUserSchema()
    return json.dumps([post_schema.dump(post) for post in posts])

@app.route('/api/v1/user/post/<int:post_id>', methods=['GET'])
def get_user_post(post_id):
    post = PostUser.query.filter(PostUser.id==user_id).order_by(PostUser.timestamp.asc()).all()
    if not user:
        return jsonify("nenhum post encontrado com esse id"), 204

    post_schema = PostUserSchema()
    return json.dumps(post_schema.dump(post)), 200

''' json model
    {
        "info": "",
        "user_id": "",
        "placa": ""
    }
    '''
@app.route('/api/v1/user/post/new', methods=['POST'])
def create_user_post():
    if not request.get_json():
        return jsonify("Requisição incompleta (json)"), 400
    if not request.json['info']:
        return jsonify("Requisição incompleta (info)"), 400
    if not request.json['user_id']:
        return jsonify("Requisição incompleta (user_id)"), 400
    if not request.json['placa']:
        return jsonify("Requisição incompleta (placa)"), 400
    
    info = request.json['info']
    user_id = request.json['user_id']
    placa = request.json['placa']

    vehicle_id = VehicleService.get_vehicle_id(placa)
    if not vehicle_id:
        return jsonify({"Erro: placa error"}), 400

    post = PostUser(info, user_id, vehicle_id)

    db.session.add(post)
    db.session.commit()
    
    post_schema = PostUserSchema()
    return json.dumps(post_schema.dump(post)), 201

@app.route('/api/v1/user/post/<int:post_id>', methods=['DELETE'])
def delete_user_post(post_id):
    post = PostUser.query.filter(PostUser.id==post_id).first()
    if not post:
        return jsonify("nenhum post_user encontrado com esse id"), 204

    db.session.delete(post)
    db.session.commit()
    post_schema = PostUserSchema()
    return json.dumps(post_schema.dump(post)), 200

@app.route('/api/v1/user/post/<int:user_id>', methods=['PUT'])
def put_user_post(post_id):
    post = PostUser.query.filter(PostUser.id==post_id).first()
    if not post:
        return jsonify("nenhum post_user encontrado com esse id"), 204
    if not request.get_json():
        return jsonify("Requisição incompleta"), 400
    
    if request.json['info']:
        user.info = request.json['info']
    if request.json['user_id']:
        user.user_id = request.json['user_id']
    if request.json['vehicle_id']:
        user.vehicle_id = request.json['vehicle_id']

    db.session.add(post)
    db.session.commit()

    post_schema = PostUserSchema()
    return json.dumps(post_schema.dump(post)), 200

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found (404)'}), 404)


