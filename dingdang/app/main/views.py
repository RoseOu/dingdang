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

# @main.route('/book/')
# def book():
#     return render_template('main/book.html')