from flask import render_template, request, redirect, url_for, flash, session, make_response
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

@app.route('/add_cookie', methods=['POST'])
def add_cookie():
    if "username" in session:
        key = request.form.get("cookie_key")
        value = request.form.get("cookie_value")
        age = int(request.form.get("cookie_age"))

        response = make_response(redirect(url_for('get_profile')))
        response.set_cookie(key, value, max_age=age)
        flash(f"Кука '{key}' успішно додана!")
        return response
    return redirect(url_for("login"))

@app.route('/delete_cookie_key', methods=['POST'])
def delete_cookie_key():
    if "username" in session:
        key = request.form.get("del_key")

        response = make_response(redirect(url_for('get_profile')))
        response.delete_cookie(key)

        flash(f"Кука '{key}' видалена!")
        return response
    return redirect(url_for("login"))

@app.route('/delete_all_cookies')
def delete_all_cookies():
    if "username" in session:
        response = make_response(redirect(url_for('get_profile')))
        for key in request.cookies.keys():
            response.delete_cookie(key)

        flash("Всі куки видалено!")
        return response
    return redirect(url_for("login"))

@app.route('/set_theme/<theme>')
def set_theme(theme):
    if "username" in session:
        response = make_response(redirect(url_for('get_profile')))
        response.set_cookie('theme', theme, max_age=30*24*60*60)
        flash(f"Вибрано тему: {theme}")
        return response
    return redirect(url_for("login"))