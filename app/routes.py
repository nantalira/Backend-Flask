from app import app, response
from app.controller import DosenController, UserController
from flask import request
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return response.success(current_user, 'Berhasil login')

@app.route('/dosen', methods=['GET', 'POST'])
@jwt_required()
def dosen():
    if request.method == 'GET':
        return DosenController.index()
    else :
        return DosenController.save()

@app.route('/dosen/<id>', methods=['GET', 'PUT', 'DELETE'])
def dosenDetail(id):
    if request.method == 'GET':
        return DosenController.detail(id)
    elif request.method == 'DELETE':
        return DosenController.delete(id)
    else :
        return DosenController.update(id)

@app.route('/createadmin', methods=['POST'])
def createAdmin():
    return UserController.buatAdmin()

@app.route('/login', methods=['POST'])
def login():
    return UserController.login()

@jwt_required()
@app.route('/logout', methods=['DELETE'])
def logout():
    return UserController.log_out()