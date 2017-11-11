#coding:utf-8

from flask import request,jsonify
from . import api
from app import db
from app.models import User,Book
from app.decorators import admin_required



#-------------Admin----------------
@api.route('/admin/test/', methods=["POST"])
@admin_required
def test():
    return "hi"

