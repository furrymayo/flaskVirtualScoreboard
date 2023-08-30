from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)


@auth.route('/')
def home():
    return "<h1>Test<h1>"

@auth.route('/Basketball')
def Basketball():
    return render_template("basketball.html")

@auth.route('/Hockey')
def Hockey():
    return render_template("hockey.html")

@auth.route('/Lacrosse')
def Lacrosse():
    return render_template("lacrosse.html")

@auth.route('/Football')
def Football():
    return render_template("football.html")

@auth.route('/Volleyball')
def Volleyball():
    return render_template("volleyball.html")

@auth.route('/Wrestling')
def Wrestling():
    return render_template("wrestling.html")

@auth.route('/Soccer')
def Soccer():
    return render_template("soccer.html")

@auth.route('/Softball')
def Softball():
    return render_template("softball.html")

@auth.route('/Baseball')
def Baseball():
    return render_template("baseball.html")
