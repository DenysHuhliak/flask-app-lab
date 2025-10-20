from flask import render_template
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
