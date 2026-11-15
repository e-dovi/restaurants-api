# __init__.py
import os
from dotenv import load_dotenv

from flask import Flask
from api.extensions import db, migrate
from api.routes import restaurants_bp
from api.config import config_map

load_dotenv()


def create_app(config_name="development"):
    app = Flask(__name__)
    app.config.from_object(config_map[config_name])

    print("DB URI:", app.config["SQLALCHEMY_DATABASE_URI"])

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(restaurants_bp)

    return app