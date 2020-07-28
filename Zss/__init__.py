from flask import Flask
from Zss.views import first_blueprint


def create_zss_app():
    app = Flask(__name__)
    app.register_blueprint(first_blueprint)
    print(app.url_map)
    return app
