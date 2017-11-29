from flask import Blueprint

api = Blueprint('api',__name__)

from . import user,book,profile,purchase,cart,order
