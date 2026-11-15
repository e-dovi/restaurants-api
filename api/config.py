import os

class Config:
    DEBUG = False
    DATABASE_URL = os.getenv("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    JWT_SECRET = os.getenv("JWT_SECRET")


class TestingConfig(Config):
    TESTING = True


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = Config.DATABASE_URL or "sqlite:///dev.db"


class ProductionConfig(Config):
    DEBUG = False


config_map = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}