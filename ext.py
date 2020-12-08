from redis import sentinel, StrictRedis
from flask import Flask
from flask_mongoengine import MongoEngine

class RedisClient:

    def __init__(self, app: Flask=None):
        if app:
            self.init_app(app)

    def init_app(self, app: Flask):
        app.rds = StrictRedis(host=app.config.get("REDIS_HOST"),
                              port=app.config.get("REDIS_PORT"))


# redis client
rds = RedisClient()


# mongo
mongo = MongoEngine()