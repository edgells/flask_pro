from flask import Flask

from ext import rds, mongo


def create_app(config_name):
    app = Flask(__name__)

    # init redis
    rds.init_app(app)
    mongo.init_app(app)

    # register blue
    register_blue(app)

    return app


def register_blue(app: Flask):
    from apps.apis.index import index
    app.register_blueprint(index)
