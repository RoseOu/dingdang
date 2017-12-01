# coding: utf-8

# config

# project base path
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """common configuration"""
    SECRET_KEY = os.environ.get("SECRET_KEY") or "hard to guess string"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    """development configuration"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DINGDANG_MYSQL_URI')
    #SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")

class TestingConfig(Config):
    """testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data-test.sqlite")
    WTF_CSRF_ENABLED = False

# production configuration
class ProductionConfig(Config):
    """production configuration"""
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.sqlite")
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    "develop": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}

