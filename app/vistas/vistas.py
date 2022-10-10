from flask_restful import Resource
from flask import request


class VistaHolaMundo(Resource):

    def post(self):
        nombre = request.json["nombre"]
        return {"message": "Hola mundo :" + nombre}, 200

class VistaPong(Resource):
    def get(self):
        return "pong",200

 