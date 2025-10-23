from . import post_bp
from flask import render_template, url_for, abort, request, redirect
from ..utils.repo import product_repo

@post_bp.route('/hi/')
@post_bp.route('/hi/<string:name>')
def greetings(name=None):
    if  name is None:
        name = ""
    name = name.upper()
    age = request.args.get("age", 0, type=int)

    return render_template("hi.html", name=name, age=age)


@post_bp.route('/admin')
def admin():
    to_url = url_for("users.greetings", name="administrator",age = 45, _external=True)
    print(to_url)
    return redirect(to_url)


@post_bp.route('/products') 
def get_products():
    products = product_repo.get_all()
    return render_template("products.html", products=products)

@post_bp.route('/product/<int:id>') 
def detail_post(id):
    if id > 3:
        abort(404)
    product = product_repo.get_by_id(id)
    return render_template("detail_post.html", product=product)