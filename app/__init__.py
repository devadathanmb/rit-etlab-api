from flask import Flask
from config import Config


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    from app.routes import status, login, profile

    app.register_blueprint(status.bp)
    app.register_blueprint(login.bp)
    app.register_blueprint(profile.bp)

    return app
