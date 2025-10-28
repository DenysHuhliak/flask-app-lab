from . import users
from flask import render_template, url_for, request, redirect, session, flash

@users.route('/hi/')
@users.route('/hi/<string:name>')
def greetings(name=None):
    if  name is None:
        name = ""
    name = name.upper()
    age = request.args.get("age", 0, type=int)

    return render_template("hi.html", name=name, age=age)

@users.route('/admin')
def admin():
    to_url = url_for("users.greetings", name="administrator",age = 45, _external=True)
    print(to_url)
    return redirect(to_url)

@users.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form["username"]
        session["username"] = username
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'secret':
            error = 'Invalid credentials'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('get_profile'))
    return render_template('login.html', error=error)

@users.route("/profile")
def get_profile():
    if "username" in session:
        username_value = session["username"]
        theme = request.cookies.get('theme', 'light')
        return render_template("profile.html", username=username_value, cookies=request.cookies, theme=theme)
    return redirect(url_for("login"))

@users.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))