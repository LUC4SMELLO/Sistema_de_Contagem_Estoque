from flask import Blueprint, request, flash, redirect, url_for, render_template

cadastro_bp = Blueprint("cadastro", __name__)

@cadastro_bp.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    return render_template("cadastro.html")