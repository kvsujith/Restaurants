import os

from flask import Flask
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix

from api import api_blueprint

PKG_NAME = os.path.split(os.path.dirname(os.path.realpath(__file__)))[-2]


def create_app(app_name=PKG_NAME):
    app = Flask(app_name)
    CORS(app)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_host=1)
    app.register_blueprint(api_blueprint)
    return app


application = create_app()
