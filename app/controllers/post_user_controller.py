from flask import Flask, json, jsonify, make_response, request, abort
from app import app, db
from app.models.post_user_model import PostUser, PostUserSchema
from app.services.vehicle_service import VehicleService

@app.route('/api/v1/postuser')
def index_post():
    return jsonify("Hi post, Welcome to Monitoramento API in Flask!")

@app.route('/api/v1/postusers', methods=['GET'])
def get_posts():
    posts = Post.query.order_by(PostUser.id.asc()).all()
    if not posts:
        abort(404)
    
    post_schema = PostUserSchema()
    return json.dumps([post_schema.dump(post) for post in posts])

@app.route('/api/v1/user/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.filter(Post.id==user_id).order_by(PostUser.timestamp.asc()).all()
    if not user:
        return jsonify("nenhum post encontrado com esse id"), 204

    post_schema = PostuserSchema()
    return json.dumps(post_schema.dump(post)), 200

@app.route('/api/v1/post/new', methods=['POST'])
def create_post():
    info = request.json['info']
    user_id = request.json['user_id']
    placa = request.json['placa']
    vehicle_id = VehicleService.get_vehicle_id(placa)
    
    if not vehicle_id:
        return jsonify({"Erro: placa error"}), 400

    post = Post(info, user_id, vehicle_id)

    db.session.add(post)
    db.session.commit()
    
    post_schema = PostUserSchema()
    return json.dumps(post_schema.dump(post)), 201

@app.route('/api/v1/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.filter(post.id==post_id).first()
    if not post:
        return jsonify("nenhum post_user encontrado com esse id"), 204

    db.session.delete(post)
    db.session.commit()
    post_schema = PostUserSchema()
    return json.dumps(post_schema.dump(post)), 200

@app.route('/api/v1/post/<int:user_id>', methods=['PUT'])
def put_post(post_id):
    post = Post.query.filter(User.id==user_id).first()
    if not post:
        return jsonify("nenhum post_user encontrado com esse id"), 204
    if not request.get_json():
        return jsonify("Requisição incompleta"), 400
    
    if request.json['username']:
        user.username = request.json['username']
    if request.json['email']:
        user.email = request.json['email']
    if request.json['senha']:
        user.senha = request.json['senha']

    db.session.add(user)
    db.session.commit()
    
    user_schema = UserSchema()
    return json.dumps(user_schema.dump(user)), 200

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error 404': 'Not found'}), 404)


