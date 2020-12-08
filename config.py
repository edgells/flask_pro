class Config:
    DEBUG = True


class DevConfig(Config):
    # redis config
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6378

    # mongo config
    MONGO_SETTINGS_DB = 'test_device_register'
    MONGO_SETTINGS_HOST = '127.0.0.1'
    MONGO_SETTINGS_PORT = 27017


class ProdConfig(Config):
    pass


config = {
    'dev': DevConfig,
    'prod': ProdConfig,
}
