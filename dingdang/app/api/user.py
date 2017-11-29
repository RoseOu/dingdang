#coding:utf-8

from flask import request,jsonify
from . import api
from app import db
from app.models import User

@api.route('/register/', methods=["POST"])
def register():
    username = request.get_json().get("username")
    email = request.get_json().get("email")
    password = request.get_json().get("password")
    if not User.query.filter_by(username=username).first() and not User.query.filter_by(email=email).first():
        user = User(username=username,email=email,password=password)
        db.session.add(user)
        db.session.commit()
        user_id=User.query.filter_by(email=email).first().id
        return jsonify({
            "user_id":user_id
            })

@api.route('/login/', methods=['POST'])
def login():
    email = request.get_json().get("email")
    password = request.get_json().get("password")
    try:
        user = User.query.filter_by(email=email).first()
    except:
        user = None
        uid = None
    if user is not None and user.verify_password(password):
        uid = user.id
        token = user.generate_auth_token()
        return jsonify({
            "user_id":user.id,
            "token":token,
            })

@api.route('/admin/login/', methods=['POST'])
def admin_login():
    email = request.get_json().get("email")
    password = request.get_json().get("password")
    try:
        user = User.query.filter_by(role_id=1).filter_by(email=email).first()
    except:
        user = None
        uid = None
    if user is not None and user.verify_password(password):
        uid = user.id
        token = user.generate_auth_token()
        return jsonify({
            "user_id":user.id,
            "token":token,
            })

