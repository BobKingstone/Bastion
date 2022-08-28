from bastion import create_flask_app, socketio
from engine.engine import engine

app = create_flask_app()

if (__name__) == "__main__":
    print("Bastion Starting ...")
    # Start ui
    # app.run(debug=True)
    socketio.run(app, debug=True)
