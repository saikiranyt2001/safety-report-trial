#done
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

def create_app():
    app = Flask(__name__)
    app.config.from_object('backend.config.Config')

    api = Api(app)
    jwt = JWTManager(app)

    api.add_resource('HelloWorld', '/hello')

    return app

app = create_app()