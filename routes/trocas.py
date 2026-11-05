from flask import Blueprint, render_template


trocas_bp = Blueprint("trocas", __name__)

@trocas_bp.route("/trocas", methods=["GET"])
def trocas():

    return render_template("trocas.html")
