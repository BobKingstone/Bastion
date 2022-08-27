from flask import Blueprint, render_template

errors = Blueprint("errors", __name__, template_folder="templates")


@errors.app_errorhandler(404)
def page_not_found(e):
    return render_template("errors/404.html")


@errors.app_errorhandler(500)
def internal_server_error(e):
    return render_template("errors/500.html")
