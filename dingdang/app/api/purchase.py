#coding:utf-8

from flask import request,jsonify
from . import api
from app import db
from app.models import User,Address
from app.decorators import admin_required

#@api.route('/admin/purchase/', methods=["GET"])
#@admin_required
#def 
