from . import post_bp
from flask import render_template, url_for, request, redirect


@post_bp.route('/hi/')
@post_bp.route('/hi/<string:name>')
def greetings(name=None):
    if  name is None:
        name = ""
    name = name.upper()
    age = request.args.get("age", 0, type=int)

    return render_template("hi.html", 
                           name=name,
                           age=age)



@post_bp.route('/admin')
def admin():
    to_url = url_for("users.greetings", name="administrator",age = 45, _external=True)
    print(to_url)
    return redirect(to_url)