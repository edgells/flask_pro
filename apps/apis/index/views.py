from flask import jsonify

from . import index


@index.route("", methods=["GET"])
def index():
    return jsonify({"data": "test"})