from flask import Blueprint, render_template, abort, jsonify
from jinja2 import TemplateNotFound
from flask_socketio import emit
from .. import socketio

from engine.engine import engine
from bastion.home import home

# handle on the underlying engine object.
engine = engine()


@home.route("/")
def index():
    try:
        return render_template("home/index.html")
    except TemplateNotFound:
        abort(404)


@home.route("/status")
def status():
    state = engine.get_status()
    return jsonify({"status": state})


@home.route("/start")
def start():
    response = engine.start()
    return jsonify({"message": response})


@home.route("/simulate")
def simulate():
    response = engine.simulate()
    return jsonify({"message": response})


@home.route("/end_simulation")
def end_simulation():
    response = engine.end_simulation()
    return jsonify({"message": response})


@home.route("/agents")
def agents():
    response = engine.get_available_agents()
    print(response)
    return jsonify(response)


@socketio.on("connect")
def connect():
    engine.attach_observer(emit_status)
    emit("status", engine.get_status())


def emit_status(msg):
    socketio.emit("status", {"msg": msg}, broadcast=True)
