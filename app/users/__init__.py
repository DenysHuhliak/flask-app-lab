from flask import Blueprint

users = Blueprint('users', __name__,template_folder="templates/users", static_folder="static")

from . import routes