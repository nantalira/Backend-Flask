import datetime
from app.model.user import User
from app import db, app, response
from config import Config
from flask import request, session
from flask_jwt_extended import *

def buatAdmin():
    try:
        nama = request.form.get('nama')
        email = request.form.get('email')
        password = request.form.get('password')
        level = 1

        user = User(nama=nama, email=email, level=level)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        return response.success('', 'Berhasil membuat admin')
    except Exception as e:
        print(e)

def singleObject(data):
    data = {
        'id': data.id,
        'nama': data.nama,
        'email': data.email,
        'level': data.level,
        'created_at': data.created_at,
        'updated_at': data.updated_at
    }
    return data

def login():
    try:
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if not user :
            return response.BadRequest([], 'Email salah')
        
        if not user.check_password(password):
            return response.BadRequest([], 'Password salah')

        data = singleObject(user)
        expires = datetime.timedelta(minutes=5)
        expires_refresh = datetime.timedelta(minutes=5)
        access_token = create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token = create_refresh_token(data, expires_delta=expires_refresh)
        print(create_access_token("nanta"))
        return response.success({
            'user': data,
            'access_token': access_token, 
            'refresh_token': refresh_token
            }, 'Berhasil login')
    except Exception as e:
        print(e)

def log_out():
    try:
        jti = get_jwt()["jti"]
        Config.set(jti, "", ex=datetime.timedelta(minutes=5))
        return response.success('', 'Berhasil logout')
    except Exception as e:
        print(e)
        