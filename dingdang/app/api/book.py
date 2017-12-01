#coding:utf-8

from flask import request,jsonify
from . import api
from app import db
from app.models import User,Book
from app.decorators import admin_required

@api.route('/book/', methods=["GET"])
def list_book():
    category = int(request.args.get("category"))
    page = int(request.args.get('page'))
    num = int(request.args.get('num')) if request.args.get('num') else 10
    if category == 0:
        book = Book.query.order_by(Book.sale.desc()).limit(num).offset((page-1)*num)
        count = Book.query.count()
    else:
        book = Book.query.filter_by(category=category).order_by(Book.sale.desc()).limit(num).offset((page-1)*num)
        count = Book.query.filter_by(category=category).count()
    book_list = [{
        "book_id":b.id,
        "name":b.name,
        "author":b.author,
        "translator":b.translator,
        "market_price":b.market_price,
        "selling_price":b.selling_price,
        "press":b.press,
        "edition":b.edition,
        "publication_time":b.publication_time,
        "version":b.version,
        "series":b.series,
        "category":b.category,
        "language":b.language,
        "binding":b.binding,
        "introduction":b.introduction,
        "catalog":b.catalog,
        "inventory":b.inventory,
        "number":b.number,
        "sale":b.sale,
        "image":b.image_url
       } for b in book]
    return jsonify({
        "book":book_list,
        "count":count
        })

@api.route('/search/', methods=["GET"])
def search_book():
    body = request.args.get("body")
    category = int(request.args.get("category"))
    page = int(request.args.get('page'))
    num = int(request.args.get('num')) if request.args.get('num') else 10
    if category==0:
        book = Book.query.filter(Book.name.like('%'+body+'%')).order_by(Book.sale.desc()).limit(num).offset((page-1)*num)
        count = Book.query.filter(Book.name.like('%'+body+'%')).count()
    else:
        book = Book.query.filter_by(category=category).filter(Book.name.like('%'+body+'%')).order_by(Book.sale.desc()).limit(num).offset((page-1)*num)
        count = Book.query.filter_by(category=category).filter(Book.name.like('%'+body+'%')).count()
    book_list = [{
        "book_id":b.id,
        "name":b.name,
        "author":b.author,
        "translator":b.translator,
        "market_price":b.market_price,
        "selling_price":b.selling_price,
        "press":b.press,
        "edition":b.edition,
        "publication_time":b.publication_time,
        "version":b.version,
        "series":b.series,
        "category":b.category,
        "language":b.language,
        "binding":b.binding,
        "introduction":b.introduction,
        "catalog":b.catalog,
        "inventory":b.inventory,
        "number":b.number,
        "sale":b.sale,
        "image":b.image_url
       } for b in book]
    return jsonify({
        "book":book_list,
        "count":count
        })

@api.route('/book/<int:id>/', methods=["GET"])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify({
        "name":book.name,
        "author":book.author,
        "translator":book.translator,
        "market_price":book.market_price,
        "selling_price":book.selling_price,
        "press":book.press,
        "edition":book.edition,
        "publication_time":book.publication_time,
        "version":book.version,
        "series":book.series,
        "category":book.category,
        "language":book.language,
        "binding":book.binding,
        "introduction":book.introduction,
        "catalog":book.catalog,
        "inventory":book.inventory,
        "number":book.number,
        "sale":book.sale,
        "image_url":book.image_url
        })

#-------------Admin----------------

@api.route('/admin/book/add/', methods=["POST"])
@admin_required
def add_book():
    name = request.get_json().get("name") if request.get_json().get("name") else ""
    author = request.get_json().get("author") if request.get_json().get("author") else ""
    translator = request.get_json().get("translator") if request.get_json().get("translator") else ""
    market_price = request.get_json().get("market_price") if request.get_json().get("market_price") else 0
    selling_price = request.get_json().get("selling_price") if request.get_json().get("selling_price") else 0
    press = request.get_json().get("press") if request.get_json().get("press") else ""
    edition = request.get_json().get("edition") if request.get_json().get("edition") else 1
    publication_time = request.get_json().get("publication_time") if request.get_json().get("publication_time") else ""
    version = request.get_json().get("version") if request.get_json().get("version") else ""
    series = request.get_json().get("series") if request.get_json().get("series") else ""
    category = request.get_json().get("category") if request.get_json().get("category") else 0
    language = request.get_json().get("language") if request.get_json().get("language") else ""
    binding = request.get_json().get("binding") if request.get_json().get("binding") else ""
    introduction = request.get_json().get("introduction") if request.get_json().get("introduction") else ""
    catalog = request.get_json().get("catalog") if request.get_json().get("catalog") else ""
    inventory = request.get_json().get("inventory") if request.get_json().get("inventory") else 0
    number = request.get_json().get("number") if request.get_json().get("number") else ""
    image_url = request.get_json().get("image_url") if request.get_json().get("image_url") else ""
    book = Book(name=name,author=author,translator=translator,market_price=market_price,
                selling_price=selling_price,press=press,edition=edition,
                publication_time=publication_time,version=version,series=series,
                language=language,binding=binding,introduction=introduction,
                catalog=catalog,inventory=inventory,number=number,image_url=image_url)
    db.session.add(book)
    db.session.commit()
    return jsonify({
        "book_id":book.id
        })


@api.route('/admin/book/<int:id>/', methods=["POST"])
@admin_required
def edit_book(id):
    book = Book.query.get_or_404(id)
    book.name = request.get_json().get("name") if request.get_json().get("name") else book.name
    book.author = request.get_json().get("author") if request.get_json().get("author") else book.author
    book.translator = request.get_json().get("translator") if request.get_json().get("translator") else book.translator
    book.market_price = request.get_json().get("market_price") if request.get_json().get("market_price") else book.market_price
    book.selling_price = request.get_json().get("selling_price") if request.get_json().get("selling_price") else book.selling_price
    book.press = request.get_json().get("press") if request.get_json().get("press") else book.press
    book.edition = request.get_json().get("edition") if request.get_json().get("edition") else book.edition
    book.publication_time = request.get_json().get("publication_time") if request.get_json().get("publication_time") else book.publication_time
    book.version = request.get_json().get("version") if request.get_json().get("version") else book.version
    book.series = request.get_json().get("series") if request.get_json().get("series") else book.series
    book.category = request.get_json().get("category") if request.get_json().get("category") else book.category
    book.language = request.get_json().get("language") if request.get_json().get("language") else book.language
    book.binding = request.get_json().get("binding") if request.get_json().get("binding") else book.binding
    book.introduction = request.get_json().get("introduction") if request.get_json().get("introduction") else book.introduction
    book.catalog = request.get_json().get("catalog") if request.get_json().get("catalog") else book.catalog
    book.inventory = request.get_json().get("inventory") if request.get_json().get("inventory") else book.inventory
    book.number = request.get_json().get("number") if request.get_json().get("number") else book.number
    book.image_url = request.get_json().get("image_url") if request.get_json().get("image_url") else book.image_url
    db.session.add(book)
    db.session.commit()
    return jsonify({
        "book_id":book.id
        })

@api.route('/admin/book/<int:id>/', methods=["DELETE"])
@admin_required
def delete_book(id):
    book = Book.query.get_or_404(id)
    if request.method == "DELETE":
        db.session.delete(book)
        db.session.commit()
        return jsonify({
            "book_id":id
            })
