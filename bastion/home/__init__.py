from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

home = Blueprint("home", __name__, template_folder="templates")

from bastion.home import views
