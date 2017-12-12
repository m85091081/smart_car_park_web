'''
@author: reimu

init for app
'''
from flask_socketio import SocketIO
from flask import Flask
from conf.api import api_verison

socketio = SocketIO()

def app_create(debug=True):
    """create runtime app"""
    app = Flask(__name__)
    app.debug = debug
    from .api.api import api
    app.register_blueprint(api, url_prefix='/api/{ver}'.format(ver=api_verison))
    socketio.init_app(app)
    return app
