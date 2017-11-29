#coding:utf-8

from flask import request,jsonify
from . import api
from app import db
from app.models import User,Book,Cart
from app.decorators import admin_required

@api.route('/cart/add/', methods=["POST"])
def add_to_cart():
    user_id = int(request.get_json().get("user_id"))
    book_id = int(request.get_json().get("book_id"))
    count = int(request.get_json().get("count"))
    if Cart.query.filter_by(user_id=user_id).filter_by(book_id=book_id).first():
        cart = Cart.query.filter_by(user_id=user_id).filter_by(book_id=book_id).first()
        cart.count = cart.count+count
    else:
        cart = Cart(user_id=user_id,book_id=book_id,count=count)
    db.session.add(cart)
    db.session.commit()
    return jsonify({
        "cart_id":cart.id
        })

@api.route('/cart/', methods=["POST"])
def show_cart():
    page = int(request.args.get('page'))
    num = int(request.args.get('num')) if request.args.get('num') else 10
    user_id = int(request.get_json().get("user_id"))
    cart = Cart.query.filter_by(user_id=user_id).limit(num).offset((page-1)*num)
    count = Cart.query.filter_by(user_id=user_id).count()
    cart_list = [{
        "cart_id":c.id,
        "name":Book.query.filter_by(id=c.book_id).first().name,
        "selling_price":Book.query.filter_by(id=c.book_id).first().selling_price,
        "count":c.count,
        "sumup":(Book.query.filter_by(id=c.book_id).first().selling_price)*(c.count),
        } for c in cart]
    return jsonify({
        "cart":cart_list,
        "count":count
        })

