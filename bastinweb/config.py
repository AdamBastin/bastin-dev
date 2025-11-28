class Config(object):
    SECRET_KEY = 'secret-shhh'

class ProductionConfig(Config):
    DEBUG = False

    # SERVER_NAME = 'bastin.dev'
    ENV = 'production'
    CACHE_TYPE = 'simple'

class DevelopmentConfig(Config):
    DEBUG = True

    SERVER_NAME = 'localhost:5000'
    ENV = 'development'
    CACHE_TYPE = 'null'

class TestingConfig(Config):
    TESTING = True
    DEBUG = True

    SERVER_NAME = 'localhost:5000'
    ENV = 'testing'
    CACHE_TYPE = 'null'