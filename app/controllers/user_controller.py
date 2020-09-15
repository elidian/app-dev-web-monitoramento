from flask import Flask, json, jsonify, make_response, request, abort
from app import app, db
from app.models.user_model import User, UserSchema

@app.route('/api/v1/user')
def index_user():
    return jsonify("Hi User, Welcome to Monitoramento API in Flask!")

@app.route('/api/v1/users', methods=['GET'])
def get_users():
    users = User.query.order_by(User.id.asc()).all()
    if not users:
        abort(404)
    
    user_schema = UserSchema()
    return json.dumps([user_schema.dump(user) for user in users])

@app.route('/api/v1/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter(User.id==user_id).first()
    if not user:
        return jsonify("nenhum user encontrado com esse id"), 204

    user_schema = UserSchema()
    return json.dumps(user_schema.dump(user)), 200

@app.route('/api/v1/user/new', methods=['POST'])
def create_user():
    username = request.json['username']
    email = request.json['email']
    senha = request.json['senha']
    user = User(username, email, senha)

    db.session.add(user)
    db.session.commit()
    
    user_schema = UserSchema()
    return json.dumps(user_schema.dump(user)), 201

@app.route('/api/v1/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.filter(User.id==user_id).first()
    if not user:
        return jsonify("nenhum user encontrado com esse id"), 204

    db.session.delete(user)
    db.session.commit()
    user_schema = UserSchema()
    return json.dumps(user_schema.dump(user)), 200

@app.route('/api/v1/user/<int:user_id>', methods=['PUT'])
def put_user(user_id):
    user = User.query.filter(User.id==user_id).first()
    if not user:
        return jsonify("nenhum user encontrado com esse id"), 204
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


