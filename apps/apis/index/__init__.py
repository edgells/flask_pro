from flask import Blueprint


index = Blueprint("index", __name__, url_prefix="/")

from . import views