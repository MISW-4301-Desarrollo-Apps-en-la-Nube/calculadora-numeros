from flask import Flask

# configura el mando de importación global
def create_app(config_name):
    app = Flask(__name__)

    return app
