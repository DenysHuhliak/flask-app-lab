from flask import Flask

app = Flask(__name__)
app.config.from_pyfile("../config.py")

from . import routes

from .users import users
app.register_blueprint(users)

from .products import products
app.register_blueprint(products)