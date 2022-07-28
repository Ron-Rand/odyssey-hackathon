import os

from flask import Flask
from extensions import *
from auth import auth
from views import views


def create_app():
    app = Flask(__name__)
    project_path = os.path.dirname(os.path.abspath("app.py"))
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{project_path}/test.db'
    app.secret_key = os.getenv("SECRET_KEY").encode()
    register_extensions(app)
    register_blueprints(app)
    db.create_all(app=app)
    return app


def register_extensions(app):
    db.init_app(app)
    sock.init_app(app)


def register_blueprints(app):
    app.register_blueprint(auth)
    app.register_blueprint(views)


if __name__ == '__main__':
    app = create_app()
