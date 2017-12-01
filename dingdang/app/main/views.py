# coding: utf-8
from . import main
from flask import render_template


# test views
@main.route('/')
def home():
    return render_template('main/index.html')

@main.route('/login/')
def login():
    return render_template('main/login.html')

