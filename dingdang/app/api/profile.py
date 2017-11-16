#coding:utf-8

from flask import request,jsonify
from . import api
from app import db
from app.models import User,Address

@api.route('/profile/<int:id>/', methods=["GET"])
def get_profile(id):
    user = User.query.get_or_404(id)
    return jsonify({
        "username":user.username,
        "email":user.email,
        "avatar":user.avatar,
        "birthday":user.birthday,
        "security_question":user.security_question
        })

@api.route('/profile/<int:id>/', methods=["PUT"])
def edit_profile(id):
    user = User.query.get_or_404(id)
    user.username = request.get_json().get("username") if request.get_json().get("username") else user.username
    user.avatar = request.get_json().get("avatar") if request.get_json().get("avatar") else user.avatar
    user.birthday = request.get_json().get("birthday") if request.get_json().get("birthday") else user.birthday
    user.security_question = request.get_json().get("security_question") if request.get_json().get("security_question") else user.security_question
    user.security_answer = request.get_json().get("security_answer") if request.get_json().get("security_answer") else user.security_answer
    return jsonify({
        "id":user.id
        })

@api.route('/profile/<int:id>/address/add/', methods=["POST"])
def add_address(id):
    user = User.query.get_or_404(id)
    location = request.get_json().get("location") if request.get_json().get("location") else ""
    phone = request.get_json().get("phone") if request.get_json().get("phone") else ""
    postcode = request.get_json().get("postcode") if request.get_json().get("postcode") else ""
    name = request.get_json().get("name") if request.get_json().get("name") else ""
    ad = [a for a in user.address]
    is_default = True if ad == [] else False
    address = Address(location=location,phone=phone,postcode=postcode,
                      name=name,is_default=is_default,user=user)
    db.session.add(address)
    db.session.commit()
    return jsonify({
        "id":address.id
        })

@api.route('/profile/<int:id>/address/', methods=["GET"])
def get_address(id):
    user = User.query.get_or_404(id)
    address = [{
        "id":a.id,
        "location":a.location,
        "phone":a.phone,
        "postcode":a.postcode,
        "name":a.name,
        "is_default":a.is_default,
        } for a in user.address]
    return jsonify({
        "address":address
        })

@api.route('/profile/<int:id>/address/set/', methods=["POST"])
def set_address(id):
    address_id = request.get_json().get("address_id")
    user = User.query.get_or_404(id)
    address = Address.query.get_or_404(address_id)
    for a in user.address:
        a.is_default = False
        db.session.add(a)
        db.session.commit()
    address.is_default = True
    db.session.add(address)
    db.session.commit()
    return jsonify({
        "id":address.id
        })

