from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.vip import VIP
from flask_app.models.adoption import Adoption


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/products")
def products():
    return render_template("products.html")


@app.route("/adopt")
def adopt():
    return render_template("adopt_a_dog.html")


@app.route("/cart")
def cart():
    return render_template("cart.html")


@app.route("/our_story")
def our_story():
    return render_template("our_story.html")


@app.route("/vip", methods=["POST"])
def vip():
    VIP.create(request.form)
    return redirect("/")

@app.route("/application")
def application():
    return render_template("application.html")

@app.route("/adoption", methods=["POST"])
def adoption():
    Adoption.create(request.form)
    return redirect("/")

@app.route("/coming_soon")
def coming_soon():
    return render_template("/coming_soon.html")