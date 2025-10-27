from flask import render_template, request, redirect, url_for, flash, session, make_response
from datetime import timedelta
from . import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/resume')
def resume():
    return render_template("resume.html")

@app.route('/contacts')
def contacts():
    return render_template("contacts.html")

@app.route('/login', methods=['GET', 'POST'])
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

@app.route("/profile")
def get_profile():
    if "username" in session:
        username_value = session["username"]
        return render_template("profile.html", username=username_value, cookies=request.cookies)
    return redirect(url_for("login"))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/set_cookie')
def set_cookie():
    response = make_response('Кука встановлена')
    response.set_cookie('username', 'student', max_age=timedelta(seconds=60))
    response.set_cookie('color', '', max_age=timedelta(seconds=60))
    return response

# @app.route('/get_cookie')
# def get_cookie():
#     username = request.cookies.get('username')
#     return f'Користувач: {username}'

# @app.route('/delete_cookie')
# def delete_cookie():
#     response = make_response('Кука видалена')
#     #response.set_cookie('username', '', expires=0) # response.set_cookie('username', '', max_age=0)
#     response.delete_cookie('color')
#     return response
@app.route('/add_cookie', methods=['POST'])
def add_cookie():
    if "username" not in session:
        return redirect(url_for("login"))

    key = request.form.get("cookie_key")
    value = request.form.get("cookie_value")
    age = int(request.form.get("cookie_age"))

    response = make_response(redirect(url_for('get_profile')))
    response.set_cookie(key, value, max_age=age)
    flash(f"Кука '{key}' успішно додана!")
    return response


@app.route('/delete_cookie_key', methods=['POST'])
def delete_cookie_key():
    if "username" not in session:
        return redirect(url_for("login"))

    key = request.form.get("del_key")

    response = make_response(redirect(url_for('get_profile')))
    response.delete_cookie(key)

    flash(f"Кука '{key}' видалена!")
    return response


@app.route('/delete_all_cookies')
def delete_all_cookies():
    if "username" not in session:
        return redirect(url_for("login"))

    response = make_response(redirect(url_for('get_profile')))
    for key in request.cookies.keys():
        response.delete_cookie(key)

    flash("Всі куки видалено!")
    return response