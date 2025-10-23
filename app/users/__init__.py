from flask import Blueprint


post_bp = Blueprint('users', __name__,template_folder="templates/users", static_folder="static")

from . import routes