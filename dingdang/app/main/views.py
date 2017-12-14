# coding: utf-8
from . import main
from flask import render_template


# test views
@main.route('/home/')
def home():
    return render_template('main/home.html')

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/login/')
def login():
    return render_template('main/login.html')

@main.route('/register/')
def register():
    return render_template('main/register.html')

@main.route('/book/<int:id>/')
def book(id):
    return render_template('main/book.html')

@main.route('/profile/<int:id>/')
def profile(id):
    return render_template('main/profile.html')

@main.route('/mycart/')
def mycart():
    return render_template('main/mycart.html')

@main.route('/order/')
def order():
    return render_template('main/order.html')

@main.route('/order/<int:id>/')
def orderdetail(id):
    return render_template('main/orderdetail.html')