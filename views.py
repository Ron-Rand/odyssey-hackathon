from flask import Blueprint, render_template, session, redirect, url_for, request
from models import Profile, Gender
from extensions import db

views = Blueprint("views", __name__)


@views.route("/")
def home():
    user = session.get("user")
    if not user:
        return redirect(url_for("auth.login"))
    return render_template("home.html", user=user)


@views.route("/create_profile", methods=["GET", "POST"])
def create_profile():
    user = session.get("user")
    if not user:
        return redirect(url_for("auth.login"))

    if request.method == "POST":
        print(request.form["gender"])
        profile = Profile(age=int(request.form["age"]), gender=Gender.from_string(request.form["gender"]), user_id=user["id"])
        db.session.add(profile)
        db.session.commit()
        session["profile"] = {"age": profile.age, "id": profile.id, "gender": str(profile.gender)}
        return redirect(url_for("views.home"))

    return render_template("create_profile.html", user=user)


@views.route("/profile")
def get_profile():
    user = session.get("user")
    if not user:
        return redirect(url_for("auth.login"))
    profile = session.get("profile")
    if not profile:
        return redirect(url_for("views.create_profile"))

    return render_template("profile.html", user=user, profile=profile)
