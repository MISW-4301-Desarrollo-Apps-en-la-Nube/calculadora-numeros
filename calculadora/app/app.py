from server import create_app
from flask_restful import Api
from .vistas import VistaHolaMundo, VistaPong


app = create_app('default')
app_context = app.app_context()
app_context.push()
app.debug = True

api = Api(app)
api.add_resource(VistaHolaMundo, '/holamundo')
api.add_resource(VistaPong, '/pong')
