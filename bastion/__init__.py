from socket import socket
from flask import Flask, Blueprint
from flask_socketio import SocketIO

socketio = SocketIO()


def create_flask_app():
    """
    Create the flask frontend app.
    """
    app = Flask(__name__)
    # app.config.from_py_file(config)
    socketio.init_app(app)

    # add extensions here e.g. db, migrate, etc.
    # Register main blueprint
    from bastion.home import home as home_blueprint

    app.register_blueprint(home_blueprint)

    # # register error handlers
    from bastion.errors import errors as errors_blueprint

    app.register_blueprint(errors_blueprint)

    return app
