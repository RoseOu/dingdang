#coding:utf-8

from flask import request,jsonify
from . import api
from app import db
from app.models import User,Book,Order,Detail,Address
from app.decorators import admin_required
from datetime import datetime,timedelta

@api.route('/order/', methods=["POST"])
def show_order():
    user_id = int(request.get_json().get("user_id"))
    status = int(request.get_json().get("status"))
    page = int(request.args.get('page'))
    num = int(request.args.get('num')) if request.args.get('num') else 10
    if status == 0:
        order = Order.query.filter_by(user_id=user_id).limit(num).offset((page-1)*num)
        count = Order.query.filter_by(user_id=user_id).count()
    else:
        order = Order.query.filter_by(user_id=user_id).filter_by(status=status).limit(num).offset((page-1)*num)
        count = Order.query.filter_by(user_id=user_id).filter_by(status=status).count()
    order_list = [{
        "order_id":o.id,
        "number":o.number,
        "freight":o.freight,
        "paynumber":o.paynumber,
        "cost":o.cost,
        "create_time":o.create_time,
        "pay_time":o.pay_time,
        "delivery_time":o.delivery_time,
        "deal_time":o.deal_time,
        "count":Detail.query.filter_by(order_id=o.id).count(),
        "name":o.name,
        "phone":o.phone,
        "location":o.location,
        "postcode":o.postcode
        } for o in order]
    return jsonify({
        "order":order_list,
        "count":count
        })

@api.route('/order/<int:id>/', methods=["GET"])
def show_detail(id):
    page = int(request.args.get('page'))
    num = int(request.args.get('num')) if request.args.get('num') else 10
    order = Order.query.filter_by(id=id).first()
    detail = Detail.query.filter_by(order_id=id).limit(num).offset((page-1)*num)
    count = Detail.query.filter_by(order_id=id).count()
    detail_list = [{
        "detail_id":d.id,
        "count":d.count,
        "cost":d.cost,
        "bookname":Book.query.filter_by(id=d.book_id).first().name,
        "image_url":Book.query.filter_by(id=d.book_id).first().image_url,
        "selling_price":Book.query.filter_by(id=d.book_id).first().selling_price
        } for d in detail]
    return jsonify({
        "detail":detail_list,
        "count":count,
        "username":order.name,
        "phone":order.phone,
        "location":order.location,
        "postcode":order.postcode
        })

@api.route('/order/create/', methods=["POST"])
def create_order():
    user_id = int(request.get_json().get("user_id"))
    order = request.get_json().get("order")
    address_id = request.get_json().get("address_id")
    freight = order["freight"]
    cost = order["cost"]
    detail = order["detail"]
    address = Address.query.filter_by(id=address_id).first()
    order = Order(freight=freight, cost=cost, status=1, name=address.name, phone=address.phone,
                  postcode=address.postcode, location=address.location, user_id=user_id,
                  create_time=(datetime.utcnow()+timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S'))
    db.session.add(order)
    db.session.commit()
    order.number = (datetime.utcnow()+timedelta(hours=8)).strftime('%Y%m%d%H%M%S') + str(order.id)
    db.session.add(order)
    db.session.commit()
    for d in detail:
        _detail = Detail(count=d["count"], cost=d["sumup"], order_id=order.id, book_id=d["book_id"])
        db.session.add(_detail)
        db.session.commit()
    return jsonify({
        "order_id":order.id
        })

@api.route('/order/pay/', methods=["POST"])
def pay_order():
    order_id = int(request.get_json().get("order_id"))
    order = Order.query.filter_by(id=order_id).first()
    order.pay_time = (datetime.utcnow()+timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    order.paynumber = (datetime.utcnow()+timedelta(hours=8)).strftime('%Y%m%d%H%M%S') + str(order.id)
    order.status = 2
    db.session.add(order)
    db.session.commit()
    return jsonify({
        "order_id":order.id,
        "pay_time":order.pay_time,
        "paynumber":order.paynumber,
        "status":order.status
        })

@api.route('/order/deal/', methods=["POST"])
def deal_order():
    order_id = int(request.get_json().get("order_id"))
    order = Order.query.filter_by(id=order_id).first()
    order.deal_time = (datetime.utcnow()+timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    order.status = 5
    db.session.add(order)
    db.session.commit()
    return jsonify({
        "order_id":order.id,
        "deal_time":order.deal_time,
        "status":order.status
        })

#-------------Admin----------------
@api.route('/admin/order/', methods=["GET"])
def get_order():
    status = int(request.args.get("status"))
    page = int(request.args.get("page"))
    num = int(request.args.get("num")) if request.args.get("num") else 10
    if status == 0:
        order = Order.query.limit(num).offset((page-1)*num)
        count = Order.query.count()
    else:
        order = Order.query.filter_by(status=status).limit(num).offset((page-1)*num)
        count = Order.query.filter_by(status=status).count()
    order_list = [{
        "order_id":o.id,
        "user_id":o.user_id,
        "freight":o.freight,
        "paynumber":o.paynumber,
        "cost":o.cost,
        "create_time":o.create_time,
        "pay_time":o.pay_time,
        "delivery_time":o.delivery_time,
        "deal_time":o.deal_time,
        "count":Detail.query.filter_by(order_id=o.id).count(),
        "name":o.name,
        "phone":o.phone,
        "location":o.location,
        "postcode":o.postcode
        } for o in order]
    return jsonify({
        "order":order_list,
        "count":count
        })

@api.route('/admin/order/delivery/', methods=["POST"])
def delivery_order():
    order_id = int(request.get_json().get("order_id"))
    order = Order.query.filter_by(id=order_id).first()
    order.delivery_time = (datetime.utcnow()+timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    order.status = 3
    db.session.add(order)
    db.session.commit()
    return jsonify({
        "order_id":order.id,
        "delivery_time":order.delivery_time,
        "status":order.status
        })



