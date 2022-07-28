from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import *

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(username=request.form["username"], password=generate_password_hash(request.form["password"]))
        db.session.add(user)
        db.session.commit()
        session["user"] = {"username": user.username, "id": user.id}
        return redirect(url_for("views.home"))
    return render_template("register.html")


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user is None or not check_password_hash(user.password, request.form["password"]):
            return render_template("login.html", error="Incorrect username or password")
        session["user"] = {"username": user.username, "id": user.id}
        return redirect(url_for("views.home"))
    return render_template("login.html")
