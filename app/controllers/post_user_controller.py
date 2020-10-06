from flask import Flask, json, jsonify, make_response, request, abort
from app import app
from app.services.post_user_service import PostService as service
from flask_login import login_required

@app.route('/api/v1/user/post')
def index_user_post():
    return jsonify("Hi user post, Welcome to Monitoramento API in Flask!")

@app.route('/api/v1/user/posts', methods=['GET'])
#@login_required
def get_user_posts():
    posts = service.get_post_list()
    if not posts:
        abort(404)
    
    return jsonify(posts), 200

@app.route('/api/v1/user/post/<int:post_id>', methods=['GET'])
#@login_required
def get_user_post(post_id):
    post = service.get_post_to_id(post_id)
    if not post:
        abort(404)

    return jsonify(post), 200

''' json model to create_user_post()
    {
        "info": "",
        "user_id": "",
        "placa": ""
    }
    '''
@app.route('/api/v1/user/post/new', methods=['POST'])
#@login_required
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
    
    post = service.set_post(info, user_id, placa)
    if post == "user_error":
        return jsonify("Erro: user_id error"), 400
    if post == "vehicle_error":
        return jsonify("Erro: vehicle error"), 400
    return jsonify(post), 201

@app.route('/api/v1/user/post/<int:post_id>', methods=['DELETE'])
#@login_required
def delete_user_post(post_id):
    post = service.delete_post(post_id)
    if not post:
        abort(404)

    return jsonify(post), 200

''' json model to put_user_post(post_id: int)
    {
        "info": "" or null,
        "cam_id": "" or null,
        "placa": "" or null
    }
    '''
@app.route('/api/v1/user/post/<int:post_id>', methods=['PUT'])
#@login_required
def put_user_post(post_id):
    if not request.get_json():
        return jsonify("Requisição incompleta"), 400
    post = service.put_post(post_id, request.get_json())
    if post is False:
        abort(403)
    if not post:
        abort(404)

    return jsonify(post), 200

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found (404)'}), 404)

@app.errorhandler(403)
def not_found(error):
    return make_response(jsonify({'error': 'Placa or User Not found (403)'}), 403)

